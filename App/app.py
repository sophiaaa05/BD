#!/usr/bin/python3
# Copyright (c) BDist Development Team
# Distributed under the terms of the Modified BSD License.
import datetime
import os
from logging.config import dictConfig
from datetime import datetime, timedelta, date

from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row
from psycopg_pool import ConnectionPool

# Use the DATABASE_URL environment variable if it exists, otherwise use the default.
# Use the format postgres://username:password@hostname/database_name to connect to the database.
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://saude:saude@postgres/saude")

pool = ConnectionPool(
    conninfo=DATABASE_URL,
    kwargs={
        "autocommit": True,  # If True don’t start transactions automatically.
        "row_factory": namedtuple_row,
    },
    min_size=4,
    max_size=10,
    open=True,
    # check=ConnectionPool.check_connection,
    name="postgres_pool",
    timeout=5,
)

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s:%(lineno)s - %(funcName)20s(): %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)
app.config.from_prefixed_env()
log = app.logger


# AUXILIAR FUNCTIONS #####################################

    
def parse_date(date):

    parsing_stuff = date.split("-")

    year, month, day = map(int, parsing_stuff)
    if not (1 <= month <= 12):
        raise ValueError("wrong month")
    if not (1 <= day <= 31):  
        raise ValueError("wrong day")

    return year, month, day

def parse_time(time):
    

    parsing_stuff = time.split(":")

    hour, minute, second = map(int, parsing_stuff)
    if not (0 <= hour < 24):
        raise ValueError("wrong hour")
    if not (0 <= minute < 60):
        raise ValueError("wrong minute")
    if not (0 <= second < 60):
        raise ValueError("wrong second")

    return hour, minute, second
def is_datetime_back_to_the_future(year, month, day, hour, minute, second):

    appointment_datetime = datetime(year, month, day, hour, minute, second)
    return appointment_datetime > datetime.now()

def generate_codigo_sns():

    with pool.connection() as conn:
        with conn.cursor() as cur:
            code = cur.execute(
                """
                SELECT codigo_sns
                FROM consulta
                ORDER BY codigo_sns DESC
                LIMIT 1;
                """,
            ).fetchone()

            return str(int(code[0]) +1 )
                
###########################################################


@app.route("/", methods=("GET",))
def list_clinics():
    """Show all the clinics, by name and address"""

    with pool.connection() as conn:
        with conn.cursor() as cur:
            clinics = cur.execute(
                """
                SELECT nome, morada
                FROM clinica;
                """,
                {},
            ).fetchall()
            log.debug(f"Found {cur.rowcount} rows.")

    return jsonify(clinics), 200

@app.route("/c/<clinica>", methods=("GET",))
def list_specialties(clinica):
    """list specialties from a specific clinic"""

    with pool.connection() as conn:
        with conn.cursor() as cur:
            especialidades = cur.execute(
                """
                SELECT DISTINCT m.especialidade
                FROM medico m
                JOIN trabalha t ON m.nif = t.nif
                JOIN clinica c ON t.nome = c.nome
                WHERE c.nome = %(clinica)s;
                """,
                {"clinica": clinica},
            ).fetchall()
            log.debug(f"Found {cur.rowcount} rows.")

    if especialidades is None:
       return jsonify({"message": "Clinic not found.", "status": "error"}), 404

    return jsonify(especialidades), 200

@app.route("/c/<clinica>/<especialidade>", methods=("GET",))
def list_all_doctors(clinica,especialidade):

    with pool.connection() as conn:
        with conn.cursor() as cur:
            especialidades = cur.execute(
                """
                SELECT DISTINCT m.especialidade
                FROM medico m
                JOIN trabalha t ON m.nif = t.nif
                JOIN clinica c ON t.nome = c.nome
                WHERE c.nome = %(clinica)s;
                """,
                {"clinica": clinica},
            ).fetchone()
            log.debug(f"Found {cur.rowcount} rows.")
        
            if especialidades is None:
                return jsonify({"message": " Specialty not found.", "status": "error"}), 404
            
            
            medicos = cur.execute(
                """
                SELECT DISTINCT m.nif
                FROM medico m, trabalha t
                WHERE m.nif = t.nif AND t.nome = %(clinica)s AND m.especialidade = %(especialidade)s;
                """,
                {"clinica": clinica, "especialidade": especialidade},
            ).fetchall()

            if len(medicos) == 0:
                return jsonify({"message": especialidade + " not found in " + clinica + ".", "status": "error"}), 404

            lista_slots = []
            for medico in medicos:
                data = date.today()
                slots_disponiveis = []
                while len(slots_disponiveis) < 3: 
                    medico_nif = medico[0]

                    slots = cur.execute(
                        """
                        SELECT m.nome, to_char(s.hora, 'HH24:MI')
                        FROM medico m, slots s, trabalha t
                        WHERE NOT EXISTS (
                            SELECT FROM consulta c
                            WHERE c.data = %(data)s AND c.hora = s.hora AND  c.nif = m.nif AND c.nome = %(clinica)s AND m.nif = %(medicoNif)s AND m.especialidade = %(especialidade)s
                        ) AND m.especialidade = %(especialidade)s AND m.nif = %(medicoNif)s AND t.nif = m.nif AND t.nome = %(clinica)s AND t.dia_da_semana = EXTRACT(DOW FROM %(data)s)
                        LIMIT 3;
                        """,
                        {"clinica": clinica, "especialidade": especialidade, "data": data.strftime("%Y-%m-%d"), "medicoNif": medico_nif},
                    ).fetchall()
                    for slot in slots:
                        slots_disponiveis += [[slot[0],slot[1],data.strftime("%Y-%m-%d")],]

                    log.debug(f"Found {cur.rowcount} rows.")
                    data += timedelta(days=1)
                lista_slots += slots_disponiveis

    return jsonify(lista_slots), 200


@app.route(
    "/a/<clinica>/registar",
    methods=(
        "PUT",
        "POST",),
)
def register_appointment(clinica):

    paciente = request.args.get("paciente")
    medico = request.args.get("medico")
    data = request.args.get("data")
    hora = request.args.get("hora")

    error = None
    
    if not paciente :
        error = "Missing field: paciente."
        
    if not medico :
        error = "Missing field: medico."
    
    if not data :
        error = "Missing field: data."
    
    if not hora:
        error = "Missing field: hora."


    if error is not None:
        return jsonify({"message": error, "status": "error"}), 400
    
    
    data = datetime.strptime(data, "%Y-%m-%d").date()
    hora = datetime.strptime(hora, "%H:%M").time()
    
    if datetime.combine(data, hora) <= datetime.now():
        return jsonify({"message": "Appointment date and time are not available, must be in the future", "status": "error"}), 400
    
    
    with pool.connection() as conn:
        with conn.cursor() as cur:
            try:
                with conn.transaction():
            
                    nome_paciente = cur.execute(
                        """
                        SELECT nome
                        FROM paciente
                        WHERE ssn = %(paciente)s""",
                        {"paciente":paciente},
                    )
                    
                    if nome_paciente is None:
                        return jsonify({"message": "Patient not Found", "status": "error"}), 404
                    
                    nome_medico = cur.execute(
                        """
                        SELECT m.nome
                        FROM medico m, trabalha t
                        WHERE m.nif = %(medico)s AND t.nif = m.nif AND t.nome = %(clinica)s AND t.dia_da_semana = EXTRACT(DOW FROM CAST(%(data)s AS DATE));""",
                        {"medico":medico, "clinica": clinica, "data":data },
                    )
                    
                    if nome_medico is None:
                        return jsonify({"message": "Doctor not Found", "status": "error"}), 404
                    
                    
                    appointment = cur.execute(
                        """
                        SELECT codigo_sns
                        FROM consulta
                        WHERE ssn = %(paciente)s AND data = %(data)s AND hora = %(hora)s;
                        """,
                        {
                            "paciente": paciente,
                            "data": data,
                            "hora": hora
                        },
                    ).fetchone()
                    
                    if appointment:
                        return jsonify({"message": "An appointment already exists for this patient at the specified date and time.", "status": "error"}), 409
                    
                    appointment = cur.execute(
                        """
                        SELECT codigo_sns
                        FROM consulta
                        WHERE nif = %(medico)s AND data = %(data)s AND hora = %(hora)s;
                        """,
                        {
                            "medico": medico,
                            "data": data,
                            "hora": hora
                        },
                    ).fetchone()
                    
                    if appointment:
                        return jsonify({"message": "An appointment already exists for this doctor at the specified date and time.", "status": "error"}), 409
                    
                    cur.execute(
                        """
                        INSERT INTO consulta (ssn,nif,nome,data,hora,codigo_sns) VALUES (%(paciente)s, %(medico)s, %(clinica)s, %(data)s, %(hora)s, %(codigo_sns)s);
                        """,
                        {
                            "paciente": paciente,
                            "medico": medico,
                            "clinica": clinica,
                            "data": data,
                            "hora": hora,
                            "codigo_sns": generate_codigo_sns(),
                        },
                    )
                    log.debug(f"Updated {cur.rowcount} rows.")

            except Exception as e:
                
                return jsonify({"message": str(e), "status": "error"}), 500
            
            else:
                

                if cur.rowcount == 0:
                    return (
                        jsonify({"message": "Appointment not found.", "status": "error"}),
                        404,
                    )
                    
    return jsonify(f"Appointment registered successfully. (Paciente: {paciente}. medico: {medico},clinica: {clinica}, data: {data}, hora: {hora})"), 200
    

@app.route(
    "/a/<clinica>/cancelar",
    methods=(
        "DELETE",
        "POST",
    ),
)
def cancel_appointment(clinica):
    """Delete the account."""
    
    paciente = request.args.get("paciente")
    medico = request.args.get("medico")
    data = request.args.get("data")
    hora = request.args.get("hora")
    
    error = None
    
    if not paciente :
        error = "Missing field: paciente."
        
    if not medico :
        error = "Missing field: medico."
    
    if not data :
        error = "Missing field: data."
    
    if not hora:
        error = "Missing field: hora."

    if error is not None:
        return jsonify({"message": error, "status": "error"}), 400
    
    data = datetime.strptime(data, "%Y-%m-%d").date()
    hora = datetime.strptime(hora, "%H:%M").time()
    
    if datetime.combine(data, hora) <= datetime.now():
        return jsonify({"message": "Appointment date and time are not available, must be in the future", "status": "error"}), 400


    with pool.connection() as conn:
        with conn.cursor() as cur:
            try:
                with conn.transaction():
                    
                    nome_paciente = cur.execute(
                        """
                        SELECT nome
                        FROM paciente
                        WHERE ssn = %(paciente)s""",
                        {"paciente":paciente},
                    )
                    
                    if nome_paciente is None:
                        return jsonify({"message": "Patient not Found", "status": "error"}), 404
                    
                    nome_medico = cur.execute(
                        """
                        SELECT nome
                        FROM medico
                        WHERE nif = %(medico)s""",
                        {"medico":medico},
                    )
                    
                    if nome_medico is None:
                        return jsonify({"message": "Doctor not Found", "status": "error"}), 404
                    
                    appointment = cur.execute(
                        """
                        SELECT codigo_sns
                        FROM consulta
                        WHERE nif = %(medico)s AND ssn = %(paciente)s AND data = %(data)s AND hora = %(hora)s;
                        """,
                        {
                            "medico": medico,
                            "paciente":paciente,
                            "data": data,
                            "hora": hora
                        },
                    ).fetchone()
                    
                    if appointment is not  None:
                        return jsonify({"message": "An appointment doesn't exist at the specified date and time.", "status": "error"}), 409
                    
                    
                    cur.execute(
                        """
                        DELETE FROM consulta
                        WHERE ssn = %(ssn)s AND nif = %(nif)s AND nome = %(clinica)s AND data = %(data)s AND hora = %(hora)s;
                        """,
                        {"ssn": paciente,"nif": medico,"clinica": clinica,"data": data,"hora": hora},
                        
                    )

            except Exception as e:
                
                return jsonify({"message": str(e), "status": "error"}), 500
            
            else:
                
                log.debug(f"Deleted {cur.rowcount} rows.")

                if cur.rowcount == 0:
                    return (
                        jsonify({"message": "Appointment not found.", "status": "error"}),
                        404,
                    )

    return jsonify(f"Appointment canceled successfully. (Paciente: {paciente}. medico: {medico},clinica: {clinica}, data: {data}, hora: {hora})"), 200

if __name__ == "__main__":
    app.run()
