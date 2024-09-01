import os
import sys
from datetime import datetime, timedelta, date
import random

FileName = os.path.dirname(os.path.abspath(sys.argv[0])) + "/populate.sql"

Robos_enfermeiros = [ "AlphaBot", "BetaBot", "GammaBot", "DeltaBot", "EpsilonBot", "ZetaBot", "EtaBot", "ThetaBot", "IotaBot", "KappaBot",
    "LambdaBot", "MuBot", "NuBot", "XiBot", "OmicronBot", "PiBot", "RhoBot", "SigmaBot", "TauBot", "UpsilonBot", "PhiBot", "ChiBot", "PsiBot", "OmegaBot", "AeroBot"
]

Robos_medicos = [ "BioBot", "CyberBot", "DataBot", "ElectroBot", "FluxBot","GeoBot", "HydroBot", "IonBot", "JetBot", "KiloBot","LaserBot", "MechaBot", "NanoBot", "OpticBot", "PlasmaBot",
    "QuantumBot", "RoboBot", "SynchroBot", "TurboBot", "UltraBot", "VortexBot", "WaveBot", "XenoBot", "YieldBot", "ZenoBot", "AquaBot", "BlazeBot", "CircuitBot", "DroneBot", "EchoBot",
    "FusionBot", "GigaBot", "HoloBot", "InfraBot", "KinetiBot", "LunaBot", "MagnaBot", "NebulaBot", "OrbitBot", "PhotonBot", "QuasarBot", "RadiantBot", "StellarBot", "TitanBot", "Unibot",
    "VitaBot", "WarpBot", "XRayBot", "ZenithBot", "AtlasBot", "BoltBot", "ChromeBot", "DynamoBot", "ElectraBot", "GyroBot", "HelixBot", "IgniteBot", "JoltBot", "KryoBot", "LeptonBot"
]

Robos_doentes = ["AlphaBot", "BetaBot", "GammaBot", "DeltaBot", "EpsilonBot", "ZetaBot", "EtaBot", "ThetaBot", "IotaBot", "KappaBot",
    "LambdaBot", "MuBot", "NuBot", "XiBot", "OmicronBot", "PiBot", "RhoBot", "SigmaBot", "TauBot", "UpsilonBot", "PhiBot", "ChiBot", "PsiBot", "OmegaBot", "AeroBot"
    "BioBot", "CyberBot", "DataBot", "ElectroBot", "FluxBot","GeoBot", "HydroBot", "IonBot", "JetBot", "KiloBot","LaserBot", "MechaBot", "NanoBot", "OpticBot", "PlasmaBot",
    "QuantumBot", "RoboBot", "SynchroBot", "TurboBot", "UltraBot", "VortexBot", "WaveBot", "XenoBot", "YieldBot", "ZenoBot", "AquaBot", "BlazeBot", "CircuitBot", "DroneBot", "EchoBot",
    "FusionBot", "GigaBot", "HoloBot", "InfraBot", "KinetiBot", "LunaBot", "MagnaBot", "NebulaBot", "OrbitBot", "PhotonBot", "QuasarBot", "RadiantBot", "StellarBot", "TitanBot", "Unibot",
    "VitaBot", "WarpBot", "XRayBot", "ZenithBot", "AtlasBot", "BoltBot", "ChromeBot", "DynamoBot", "ElectraBot", "GyroBot", "HelixBot", "IgniteBot", "JoltBot", "KryoBot", "LeptonBot",
    "Wall-E", "Sonny", "David", "Bumblebee", "Ultron", "Andrew Martin", "Gort", "Ash", "T-800", "Pris", "Baymax", "Robby", "Marvin", "C-3PO", "R2-D2", "BB-8"]

star_wars_addresses_and_spaceships = ["Tatooine", "Coruscant", "Naboo", "Hoth", "Dagobah", "Endor", "Alderaan", "Mustafar", "Kashyyyk", "Kamino",
    "Bespin", "Geonosis", "Jakku", "Ahch-To", "D Qar", "Crait", "Scarif", "Lothal", "Mandalore", "Kessel", 
    "Corellia", "Felucia", "Hosnian Prime", "Yavin 4", "Jedha", "Sullust", "Umbara", "Ilum", "Mygeeto", "Utapau", 
    "Saleucami", "Rodia", "Mon Cala", "Mustafar", "Ryloth", "Dantooine", "Malachor", "Tython", "Exegol", 
    "Ord Mantell", "Nal Hutta", "Onderon", "Serenno", "Vardos", "Takodana", "Pasaana", "Lah mu", "Kijimi", 
    "Eadu", "Jedha City", "Niima Outpost", "Fathiers", "Cantonica", "Cantonica City", "Canto Bight", "Sorgan", 
    "Ferrix", "Nevarro", "Tython", "Rishi", "Korriban", 
    "Millennium Falcon", "X-Wing", "TIE Fighter", "Star Destroyer", "Death Star", "Slave I", "A-Wing", "B-Wing", 
    "Y-Wing", "Imperial Shuttle", "Nebulon-B Frigate", "Mon Calamari Cruiser", "Jedi Starfighter", "Droid Starfighter", 
    "Sandcrawler", "Republic Gunship", "Sith Infiltrator", "Vulture Droid", "Venator-class Star Destroyer", 
    "ARC-170 Starfighter", "N-1 Starfighter", "Resistance Bomber", "U-Wing", "Tantive IV", "Home One", "Ghost", 
    "Outrider", "Ebon Hawk", "Razor Crest", "Slave II", "TIE Interceptor", "TIE Bomber", "Imperial Landing Craft"
]

filmes_star_wars = [
    "Star Wars: Episodio IV - Uma Nova Esperanca",
    "Star Wars: Episodio V - O Imperio Contra-Ataca",
    "Star Wars: Episodio VI - O Retorno de Jedi",
    "Star Wars: Episodio I - A Ameaca Fantasma",
    "Star Wars: Episodio II - O Ataque dos Clones",
    "Star Wars: Episodio III - A Vinganca dos Sith",
    "Star Wars: O Despertar da Forca",
    "Rogue One: Uma Historia Star Wars",
    "Star Wars: Os Ultimos Jedi",
    "Han Solo: Uma Historia Star Wars",
    "Star Wars: A Ascensao Skywalker",
    "Lisboa"
]

Especialidades = ["circuit diagnostics", "fluid dynamics", "thermal management", "cardiologia","ortopedia"]

Sintomas = ["Overheating", "LowBattery", "CircuitFault", "MemoryLeak", "MotorMalfunction", "SensorFailure", "NetworkLoss", "SignalInterference",
                 "SoftwareCrash", "HardwareFailure", "PowerSurge", "VoltageDrop", "ThermalThrottling", "ProcessorOverload", "ActuatorStuck", "GyroscopeError",
                 "CameraObstruction", "ServoJam", "HydraulicLeak", "PneumaticFailure", "OpticsMisalignment", "AudioDistortion", "LowTorque", "HighFriction",
                 "JointWear", "MechanicalSlack", "LubricantDepletion", "BearingFailure", "ThermalExpansion", "Oscillation", "Resonance", "Contamination",
                 "Corrosion", "SignalDelay", "DataCorruption", "FeedbackLoopError", "ActuatorDrift", "SensorDrift", "MemoryOverflow", "PacketLoss", "FirmwareBug",
                 "AlignmentError", "Stiction", "StaticDischarge", "ElectromagneticInterference", "CoolingFailure", "MagneticFieldDisruption", "CalibrationError",
                 "LoadImbalance", "StructuralFatigue"]

robot_symptoms = ["Overheating", "Abnormal vibration", "Connection error", "Communication failure", 
                  "Power loss", "Excessive noise", "Premature wear", "Corrosion", "Material fatigue",
                  "Sensor failure", "Calibration error", "Overload", "Misalignment", "Software error", 
                  "Short circuit", "Current leakage", "Actuator failure", "Unstable oscillation", 
                  "Increased resistance", "Motor failure", "Battery drainage", "Reading error", "System freezing", 
                  "Reduced performance", "Boot failure", "Memory failure", "Temperature error", "Network issue", 
                  "Synchronization error", "Latency increase", "Command failure", "Data loss", "Response failure", 
                  "Registration error", "Signal noise", "Protocol error", "Security breach", "Fluid leakage", 
                  "Detection error", "Torque issue", "Cable wear", "Gyroscope failure", "Navigation problem", 
                  "Orientation error", "Stabilization issue", "Bearing wear", "Pressure problem", "Configuration error", 
                  "Ventilation failure"]

robot_metric_observations = ["Motor temperature", "Operating voltage", "Electric current", 
                             "Rotation speed", "Vibration frequency", "Noise level", "Battery capacity",
                             "Response time", "Applied force", "Movement precision", "Communication latency", 
                             "Power consumption", "Hydraulic pressure", "Generated torque", "Electric resistance", 
                             "Pulse frequency", "Wear index", "Navigation stability", "Gyroscope reading", "Lubrication level"]

horarios = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', 
            '11:00', '11:30', '12:00', '12:30', '14:00', '14:30', '15:00', 
            '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30']

horarios_2 = ['8:00', '8:30', '9:00', '9:30', '8:00', '8:30', '9:00', '9:30', '10:00', '10:30', 
            '11:00', '11:30', '12:00', '12:30', '14:00', '14:30', '15:00', 
            '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30']

medicamentos_para_robos = ["RoboMax-500", "NanoLubricant-X", "CyberVitaGel", "MechaRepair-Plus", 
                           "OptiCircuit Serum", "SynthOil-3000", "ElectroGuard-10", "NanoFix-200",
                           "BioBot-Energizer", "HoloLens Cleaner", "QuantumCoolant", "ServoBoost-7", 
                           "CircuitRevive", "MechaElixir", "BotRefuel-X", "TechRegen Solution", "RoboRepair-Nano", 
                           "SynthCircuit Enhancer", "MechaBalm", "ElectroRepair Serum", "WD-40"]


global_id_consulta = 1
##################################################### AUX GENERATE ##################################################################
existing_nif_numbers = []
existing_ssn_numbers = []
existing_code_sns = []
moradas_clinicas = []


def GenName(name: str, version: int, edition: int) -> str:
    name2 = ""
    name2 += name + " " + str(version) + "." + str(edition)
    return name2

def GenerateNifNumbers() -> int:
    global existing_nif_numbers
    while True:
        new_number = random.randint(100000000, 999999999) 
        if new_number not in existing_nif_numbers:
            existing_nif_numbers.append(new_number)
            return new_number

def GenerateSsnNumbers() -> int:
    global existing_ssn_numbers
    while True:
        new_number = random.randint(10000000000, 99999999999) 
        if new_number not in existing_ssn_numbers:
            existing_ssn_numbers.append(new_number)
            return new_number
        
def GenerateSnsNumbers() -> int:
    global existing_code_sns
    while True:
        new_number = random.randint(100000000000, 999999999999) 
        if new_number not in existing_ssn_numbers:
            existing_ssn_numbers.append(new_number)
            return new_number

def GenerateRecepiesN(x, y) -> int:
    return random.randint(x, y) 

def GeneratePhoneNumbers() -> int:
    return random.randint(910000000, 990000000) 
        
def GenerateAdress() -> str:
    adress_funcional = False
    while not adress_funcional:
        endereco = random.choice(star_wars_addresses_and_spaceships)
        primeiro_grupo = f"{random.randint(1, 9):d}{random.randint(0, 9):d}{random.randint(0, 9):d}{random.randint(0, 9):d}"
        segundo_grupo = f"{random.randint(0, 9):d}{random.randint(0, 9):d}{random.randint(0, 9):d}"
        codigo_postal = f"{primeiro_grupo}-{segundo_grupo}"
        filme = random.choice(filmes_star_wars)
        adress = f"{endereco}, {codigo_postal}, {filme}"
        if(adress not in moradas_clinicas):
            adress_funcional = True
            
    return adress

def GenerateClinAdress(local:str) -> str:
    adress_funcional = False
    while not adress_funcional:
        endereco = random.choice(star_wars_addresses_and_spaceships)
        primeiro_grupo = f"{random.randint(1, 9):d}{random.randint(0, 9):d}{random.randint(0, 9):d}{random.randint(0, 9):d}"
        segundo_grupo = f"{random.randint(0, 9):d}{random.randint(0, 9):d}{random.randint(0, 9):d}"
        codigo_postal = f"{primeiro_grupo}-{segundo_grupo}"
        adress = f"{endereco}, {codigo_postal} ,{local}"
        if(adress not in moradas_clinicas):
            moradas_clinicas.append(adress)
            adress_funcional = True

    return f"{endereco}, {codigo_postal} ,{local}"

def GenerateBirthDate(start_year=1924, end_year=2022):
    # Generate a random number of days between the start date and end date
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta_days = (end_date - start_date).days

    random_days = random.randint(0, delta_days)
    random_date = start_date + timedelta(days=random_days)

    # Return the date in "YYYY-M-D" format
    return random_date.strftime("%Y-%m-%d").replace('-0', '-')
    
    
##################################################### AUX INSERT ####################################################################
def InsertData(list:list,file):
    file.write("(")
    max = list.__len__()
    for x in range(0,max):
        if(isinstance(list[x],str)):
            file.write("'"+list[x]+"'")
        else:
            file.write(str(list[x]))
        if(max != x + 1):
            file.write(",")
    file.write(")")
    
def InsertVarius(list:list,file):
    max = list.__len__()
    for x in range(0,max):
        list[x].PrintToFile(file)
        if(max != x + 1):
            file.write(",\n")

##################################################### GENERATE DATA ####################################################################

###### PRINT TABLE ######

class TableObject:
    def PrintToFile(file):
        raise Exception("YOU IDIOT! define this - in honor Antunes")

###### PRINT CLINICAS ######
class Clinica(TableObject):
    def __init__(self,nome:str,telefone:int,morada:str):
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        
    def PrintToFile(self,file):
        InsertData([str(self.nome),str(self.telefone),str(self.morada)],file)
        pass
    
clinicas = []
adress = GenerateClinAdress("Lisboa")
clinicas.append(Clinica("TechCare", "980567345", adress))
adress = GenerateClinAdress("Lisboa")
clinicas.append(Clinica("RoboHealth", "934234567", adress))
adress = GenerateClinAdress("Lisboa")
clinicas.append(Clinica("AI Medics", "921345698", adress))
adress = GenerateClinAdress("Star Wars: Episodio IV - Uma Nova Esperanca")
clinicas.append(Clinica("CyberMed", "908756345", adress))
adress = GenerateClinAdress("Rogue One: Uma Historia Star Wars")
clinicas.append(Clinica("NanoClinic", "934567123", adress))

###### PRINT ENFERMEIROS ######

class Enfermeiro(TableObject):
    def __init__(self, nif:str, nome:str, telefone:str, morada:str, nome_clinica:str):
        self.nif = nif
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        self.nome_clinica = nome_clinica
        
    def PrintToFile(self,file):
        InsertData([str(self.nif),str(self.nome),str(self.telefone),str(self.morada),str(self.nome_clinica)],file)
        pass

Enfermeiros = []
i = 0
for clin in clinicas:
    for num in range(5):
        Enfermeiros.append(Enfermeiro(GenerateNifNumbers(),GenName(Robos_enfermeiros[num + i * 5], 0, 0),GeneratePhoneNumbers(),GenerateAdress(),clin.nome))
    i += 1

###### PRINT MEDICO ######

class Medico(TableObject):
    def __init__(self,nif:str,nome:str,telefone:str,morada:str,especialidade:str):
        self.nif = nif
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        self.especialidade = especialidade
        
    def PrintToFile(self,file):
        InsertData([str(self.nif),str(self.nome),str(self.telefone),str(self.morada),str(self.especialidade)],file)
        pass

Medicos = []
for num in range(20):
        Medicos.append(Medico(GenerateNifNumbers(),GenName(Robos_medicos[num], 0, 0),GeneratePhoneNumbers(),GenerateAdress(),"clínica geral"))
for num in range(40):
        Medicos.append(Medico(GenerateNifNumbers(),GenName(Robos_medicos[num + 20], 0, 0),GeneratePhoneNumbers(),GenerateAdress(),random.choice(Especialidades)))

###### PRINT TRABALHA ######

class Trabalha(TableObject):
    def __init__(self,nif:str,nome:str,dia_da_semana:int):
        self.nif = nif
        self.nome = nome
        self.dia_da_semana = dia_da_semana
        
    def PrintToFile(self,file):
        InsertData([str(self.nif),str(self.nome),str(self.dia_da_semana)],file)
        pass

Trabalhas = []
medCounter = 0
clinCounter = 0

for day in range(7):
    i = 0
    robot_ocupied = []  
    if day == 1 or day == 0: 
        for med in Medicos:
            Trabalhas.append(Trabalha(med.nif, clinicas[(i + day) % len(clinicas)].nome, day))
            i += 1
    else:
        for clin in clinicas:
            j = 0
            while j < 8: # cada clinica tem de ter 8 medicos por dia 
                med = random.choice(Medicos)
                if med.nif not in robot_ocupied:
                    Trabalhas.append(Trabalha(med.nif, clin.nome, day))
                    robot_ocupied.append(med.nif)
                    j += 1

###### PRINT PACIENTES ######
      
Pacientes = []
class Paciente(TableObject):
    def __init__(self,ssn:str,nif:str,nome:str,telefone:str,morada:str,data_nasc:str):
        self.ssn = ssn
        self.nif = nif
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        self.data_nasc = data_nasc
        
    def PrintToFile(self,file):
        InsertData([str(self.ssn),str(self.nif),str(self.nome),str(self.telefone),str(self.morada),str(self.data_nasc)],file)
        pass

Pacientes = []      
for enfermeiro in Enfermeiros:
    Pacientes.append(Paciente(GenerateSsnNumbers(),enfermeiro.nif,enfermeiro.nome,enfermeiro.telefone,enfermeiro.morada,GenerateBirthDate()))
    
for med in Medicos:
    Pacientes.append(Paciente(GenerateSsnNumbers(), med.nif, med.nome, med.telefone, med.morada, GenerateBirthDate()))

version = 1 
edition = 0
iteration = 0
for num in range(85, 5000):
        Pacientes.append(Paciente(GenerateSsnNumbers(),GenerateNifNumbers(),GenName(Robos_doentes[num % 100], version, edition),GeneratePhoneNumbers(),GenerateAdress(),GenerateBirthDate()))
        if iteration == 99:
            edition += 1
            iteration = 0
        if edition == 10:
            version += 1
            edition = 0
        iteration += 1

###### PRINT CONSULTA ######

class Consulta(TableObject):
    def __init__(self,ssn:str,nif:str,nome:str,data:str,hora:str,codigo_sns:str, _id: int):
        self.id = _id
        self.ssn = ssn
        self.nif = nif
        self.nome = nome
        self.data = data
        self.hora = hora
        self.codigo_sns = codigo_sns
        
        
    def PrintToFile(self,file):
        InsertData([str(self.ssn),str(self.nif),str(self.nome),str(self.data),str(self.hora),str(self.codigo_sns)],file)
        pass

Consultas = []

def create_cons_2(inicio: int, fim: int, current_date: date, robos_concertados_dia: list):
    
    global global_id_consulta
    for clin in clinicas:
        i = 0
        j = 0
        while i != 2:
            
            for trabalho in Trabalhas[inicio:fim]:
                
                if trabalho.nome == clin.nome:
                    paciente_encontrado = False
                    while not paciente_encontrado:
                        paciente = random.choice(Pacientes)
                        if paciente.nif not in robos_concertados_dia:
                            robos_concertados_dia.append(paciente.nif)
                            Consultas.append(Consulta(paciente.ssn, trabalho.nif, clin.nome, current_date, horarios_2[j], GenerateSnsNumbers(), global_id_consulta))
                            global_id_consulta += 1
                            j += 1
                            paciente_encontrado = True
            
            i += 1
                    
def create_consulta (dias_ano: list, year: int):
    
    global global_id_consulta
    for month in range(1, len(dias_ano) + 1):
        for day in range(1, dias_ano[month - 1] + 1):
            
            robos_concertados_dia = []
            
            current_date = date(year, month, day)
            day_of_week = current_date.weekday()
            
            if day_of_week == 0:
                create_cons_2(0, 60, current_date, robos_concertados_dia)
                continue
            
            elif day_of_week == 1:
                create_cons_2(61, 120, current_date, robos_concertados_dia)
                continue
            
            else:
                j = 0
                while j != 5:
                    i = 0
                    while i != 20:
                        for num in range(8):
                            medico = Trabalhas[num + 120 + (day_of_week - 2) * 40 + j * 8]
                            nif_doc = medico.nif
                            clin = medico.nome

                            paciente_encontrado = False
                            while not paciente_encontrado:
                                paciente = random.choice(Pacientes)
                                if paciente.nif not in robos_concertados_dia:
                                    robos_concertados_dia.append(paciente.nif)
                                    Consultas.append(Consulta(paciente.ssn, nif_doc, clin, current_date, horarios[i], GenerateSnsNumbers(), global_id_consulta))
                                    global_id_consulta += 1
                                    i += 1
                                    paciente_encontrado = True
                            
                            if i == 20:                               
                                break
                    j += 1        

# 2023
dias_2023 = [31,28,31,30,31,30,31,31,30,31,30,31]
create_consulta(dias_2023, 2023)
# 2023
dias_2024 = [31,29,31,30,31,30,31,31,30,31,30,31]
create_consulta(dias_2024, 2024)

###### PRINT RECEITAS ######

class Receita(TableObject):
    def __init__(self, ssn:str, med:str, quant:int):
        self.ssn = ssn
        self.med = med
        self.quant = quant
        
    def PrintToFile(self,file):
        InsertData([str(self.ssn), str(self.med), str(self.quant)],file)
        pass

Receitas = []   
num_receitas = int(9028 * 0.8)


for consulta in Consultas[0:num_receitas]:
    type_medicamento = []
    num_meds = GenerateRecepiesN(1,6)
    for i in range(num_meds):
        med_found = False
        while not med_found:
            medicamento_aleatorio = random.choice(medicamentos_para_robos)
            if(medicamento_aleatorio not in type_medicamento):
                type_medicamento.append(medicamento_aleatorio)
                quant = GenerateRecepiesN(1, 3)
                Receitas.append(Receita(consulta.codigo_sns, medicamento_aleatorio ,quant))
                med_found = True
 
###### PRINT SINTOMAS ######

class Sintoma(TableObject):
    def __init__(self, id_ :int, parametro:str):
        self.id = id_
        self.parametro = parametro
        self.value = 0.0
        
    def PrintToFile(self,file):
        InsertData([str(self.id), str(self.parametro), self.value],file)
        pass

Sintomas = []   

for consulta in Consultas[0:9028]:
    type_symptom = []
    num_sintomas = GenerateRecepiesN(1,5)
    for i in range(num_sintomas):
        synt_found = False
        while not synt_found:
            sintoma_aleatorio = random.choice(robot_symptoms)
            if(sintoma_aleatorio not in type_symptom):
                type_symptom.append(sintoma_aleatorio)
                Sintomas.append(Sintoma(consulta.id, sintoma_aleatorio))
                synt_found = True
        
###### PRINT OBSERVACAO ######
class Observacao(TableObject):
    def __init__(self, id_ :int, parametro:str, valor:float):
        self.id = id_
        self.parametro = parametro
        self.valor = valor
        
    def PrintToFile(self,file):
        InsertData([str(self.id), str(self.parametro), self.valor ],file)
        pass

Observacoes = []  

for consulta in Consultas[0:9028]:  # Iterar sobre todas as consultas
    type_observacao = []
    num_observacao = GenerateRecepiesN(0, 3)
    for i in range(num_observacao):
        obs_found = False
        while not obs_found:
            obs_aleatoria = random.choice(robot_metric_observations)
            if obs_aleatoria not in type_observacao:
                type_observacao.append(obs_aleatoria)
                valor = random.random() * 100
                Observacoes.append(Observacao(consulta.id, obs_aleatoria , valor))
                obs_found = True

                            
##################################################### PRINT FILE ####################################################################
                 
file = open(FileName,"w")

file.write("INSERT INTO clinica (nome,telefone,morada)\nVALUES\n")
InsertVarius(clinicas,file)
file.write(";\n")

file.write("INSERT INTO enfermeiro (nif,nome,telefone,morada,nome_clinica)\nVALUES\n")
InsertVarius(Enfermeiros,file)
file.write(";\n")

file.write("INSERT INTO medico (nif,nome,telefone,morada,especialidade)\nVALUES\n")
InsertVarius(Medicos,file)
file.write(";\n")

file.write("INSERT INTO trabalha (nif,nome,dia_da_semana)\nVALUES\n")
InsertVarius(Trabalhas,file)
file.write(";\n")

file.write("INSERT INTO paciente (ssn,nif,nome,telefone,morada,data_nasc)\nVALUES\n")
InsertVarius(Pacientes,file)
file.write(";\n")

file.write("INSERT INTO consulta (ssn,nif,nome,data,hora,codigo_sns)\nVALUES\n")
InsertVarius(Consultas,file)
file.write(";\n")

file.write("INSERT INTO receita (codigo_sns, medicamento, quantidade)\nVALUES\n")
InsertVarius(Receitas,file)
file.write(";\n")

file.write("INSERT INTO observacao (id, parametro, valor)\nVALUES\n")
InsertVarius(Sintomas,file)
file.write(",\n")
InsertVarius(Observacoes,file)
file.write(";\n")

file.close()
