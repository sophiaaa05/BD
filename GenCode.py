
import os
import sys
import random
import math

FileName = os.path.dirname(os.path.abspath(sys.argv[0])) + "/populate.sql"

Names = ["AlphaBot", "BetaBot",
              "GammaBot", "DeltaBot", "EpsilonBot", "ZetaBot", "EtaBot", "ThetaBot", "IotaBot", "KappaBot",
              "LambdaBot", "MuBot", "NuBot", "XiBot", "OmicronBot", "PiBot", "RhoBot", "SigmaBot", "TauBot", "UpsilonBot",
              "PhiBot", "ChiBot", "PsiBot", "OmegaBot",
              "AeroBot", "BioBot", "CyberBot", "DataBot", "ElectroBot", "FluxBot", "GeoBot", "HydroBot", "IonBot", "JetBot",
              "KiloBot", "LaserBot", "MechaBot", "NanoBot", "OpticBot", "PlasmaBot", "QuantumBot", "RoboBot", "SynchroBot",
              "TurboBot", "UltraBot", "VortexBot", "WaveBot", "XenoBot", "YieldBot", "ZenoBot", "AquaBot", "BlazeBot", 
              "CircuitBot", "DroneBot", "EchoBot", "FusionBot", "GigaBot", "HoloBot", "InfraBot", "JetBot", "KinetiBot",
              "LunaBot", "MagnaBot", "NebulaBot", "OrbitBot", "PhotonBot", "QuasarBot", "RadiantBot", "StellarBot", 
              "TitanBot", "Unibot", "VitaBot", "WarpBot", "XRayBot", "ZenithBot", "AtlasBot", "BoltBot", "ChromeBot",
              "DynamoBot", "ElectraBot", "FluxBot", "GyroBot", "HelixBot", "IgniteBot", "JoltBot", "KryoBot", "LeptonBot",
              "MagnetoBot", "NebulaBot", "OculusBot", "PulseBot", "QuantaBot", "RayBot", "StarkBot", "TitanBot",
              "UltraBot", "VectorBot", "WaveBot", "XenoBot", "YottaBot", "ZephyrBot", "ApolloBot", "BlazeBot",
              "CobaltBot", "DynamoBot", "EonBot", "FluxBot", "GigaBot", "HelixBot", "IgniteBot", "JetBot", "KryptonBot"]

Moradas = ["Servo", "Bolt", "Circuit", "Drone", "Echo", "Fusion", "Giga", "Helix", "Ignite", "Jet", 
                     "Kryo", "Luna", "Magna", "Nebula", "Optic", "Photon", "Quasar", "Radiant", "Stellar", "Titan", 
                     "Ultra", "Vortex", "Warp", "XRay"]

Especialidades = ["circuit diagnostics", "fluid dynamics", "thermal management", "aerospace maintenance","medical assistance"]

Sintomas = ["Overheating", "LowBattery", "CircuitFault", "MemoryLeak", "MotorMalfunction", "SensorFailure", "NetworkLoss", "SignalInterference",
                 "SoftwareCrash", "HardwareFailure", "PowerSurge", "VoltageDrop", "ThermalThrottling", "ProcessorOverload", "ActuatorStuck", "GyroscopeError",
                 "CameraObstruction", "ServoJam", "HydraulicLeak", "PneumaticFailure", "OpticsMisalignment", "AudioDistortion", "LowTorque", "HighFriction",
                 "JointWear", "MechanicalSlack", "LubricantDepletion", "BearingFailure", "ThermalExpansion", "Oscillation", "Resonance", "Contamination",
                 "Corrosion", "SignalDelay", "DataCorruption", "FeedbackLoopError", "ActuatorDrift", "SensorDrift", "MemoryOverflow", "PacketLoss", "FirmwareBug",
                 "AlignmentError", "Stiction", "StaticDischarge", "ElectromagneticInterference", "CoolingFailure", "MagneticFieldDisruption", "CalibrationError",
                 "LoadImbalance", "StructuralFatigue"]

Metricas =  ["Metric-Alpha", "Metric-Beta", "Metric-Gamma", "Metric-Delta", "Metric-Epsilon", "Metric-Zeta", "Metric-Eta", 
                "Metric-Theta", "Metric-Iota", "Metric-Kappa", "Metric-Lambda", "Metric-Mu", "Metric-Nu", "Metric-Xi", 
                "Metric-Omicron", "Metric-Pi", "Metric-Rho", "Metric-Sigma", "Metric-Tau", "Metric-Upsilon"]

def GenData():
    Year = random.randrange(800,1900)
    M = random.randrange(1,12)
    Day = random.randrange(1,20)#too lazy
    return str(Year)+"-"+str(M)+"-"+str(Day)

def GenList(list:list):
    num = random.randrange(0,list.__len__())
    return list[num]

def GenName():
    name = ""
    num = random.randrange(0,Names.__len__())
    name += Names[num] + "-" + str(random.randint(1,10))
    return name

def GenMorada():
    num = random.randrange(0,Moradas.__len__())
    strada = Moradas[num]
    hash = abs(strada.__hash__())
    first = hash%(10000-1000)+1000
    last = (hash>>4)%(1000-100)+100
    return str(first)+"-"+str(last)+" "+strada

def GenNum(target:int):
    t = 10**target
    num = random.randint(0,t)
    num = (num%(t-t/10)+t/10)
    return str(math.floor(num))

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

class TableObject:
    def PrintToFile(file):
        raise Exception("YOU IDIOT! define this")

class Clinica(TableObject):
    def __init__(self,nome:str,telefone:int,morada:str):
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        
    def PrintToFile(self,file):
        InsertData([self.nome,self.telefone,self.morada],file)
        pass

class Enfermeiro(TableObject):
    def __init__(self,nif:str,nome:str,telefone:str,morada:str,nome_clinica:str):
        self.nif = nif
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        self.nome_clinica = nome_clinica
        
    def PrintToFile(self,file):
        InsertData([self.nif,self.nome,self.telefone,self.morada,self.nome_clinica],file)
        pass

class Medico(TableObject):
    def __init__(self,nif:str,nome:str,telefone:str,morada:str,especialidade:str):
        self.nif = nif
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        self.especialidade = especialidade
        
    def PrintToFile(self,file):
        InsertData([self.nif,self.nome,self.telefone,self.morada,self.especialidade],file)
        pass

class Trabalha(TableObject):
    def __init__(self,nif:str,nome:str,dia_da_semana:str):
        self.nif = nif
        self.nome = nome
        self.dia_da_semana = dia_da_semana
        
    def PrintToFile(self,file):
        InsertData([self.nif,self.nome,self.dia_da_semana,],file)
        pass

class Paciente(TableObject):
    def __init__(self,ssn:str,nif:str,nome:str,telefone:str,morada:str,data_nasc:str):
        self.ssn = ssn
        self.nif = nif
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        self.data_nasc = data_nasc
        
    def PrintToFile(self,file):
        InsertData([self.ssn,self.nif,self.nome,self.telefone,self.morada,self.data_nasc],file)
        pass

class Consulta(TableObject):
    def __init__(self,ssn:str,nif:str,nome:str,data:str,hora:str,codigo_sns:str):
        self.ssn = ssn
        self.nif = nif
        self.nome = nome
        self.data = data
        self.hora = hora
        self.codigo_sns = codigo_sns
        
    def PrintToFile(self,file):
        InsertData([self.ssn,self.nif,self.nome,self.data,self.hora,self.codigo_sns],file)
        pass


clinicas = []
clinicas.append(Clinica("TechCare", "980567345", "Silicon Valley"))
clinicas.append(Clinica("RoboHealth", "934234567", "Cybernetic Street"))
clinicas.append(Clinica("AI Medics", "921345698", "Mainframe Avenue"))
clinicas.append(Clinica("CyberMed", "908756345", "Data Drive"))
clinicas.append(Clinica("NanoClinic", "934567123", "Byte Lane"))

Enfermeiros = []
for clin in clinicas:
    for num in range(5):#5-6
        Enfermeiros.append(Enfermeiro(GenNum(9),GenName(),GenNum(9),GenMorada(),clin.nome))

Medicos = []
for num in range(20):
        Medicos.append(Medico(GenNum(9),GenName(),GenNum(9),GenMorada(),"clínica geral"))
for num in range(40):
        Medicos.append(Medico(GenNum(9),GenName(),GenNum(9),GenMorada(),GenList(Especialidades)))

rollingcounter = 0

Trabalhas = []
for clin in clinicas:
    for day in range(7):
        for num in range(8):
            rollingcounter=(rollingcounter+1)%Medicos.__len__()
            Trabalhas.append(Trabalha(Medicos[rollingcounter].nif,clin.nome,day))
        rollingcounter +=4

Pacientes = []
for num in range(5000):
        Pacientes.append(Paciente(GenNum(11),GenNum(9),GenName(),GenNum(9),GenMorada(),GenData()))

fuck = [31,28,31,30,31,30,31,31,30,31,30,31]

def SandMyballs(num:int):
    i = 0
    date = "2023"
    mouth = 0
    day = num
    while(1):
        if(day>=fuck[i]):
            day = day-fuck[i]
            i+=1
            mouth+=1
        else:
            break
    return date + "-" + str(mouth+1) + "-" + str(day+1)

Consultas = []
for day in range(365):
    for clin in clinicas:
        for num in range(20):
            Consultas.append(Consulta("0","0",clin.nome,SandMyballs(day),"12:00",GenNum(12)))

#TODO Deal Whit Collisions nif

file = open(FileName,"w")

file.write("INSERT INTO clinica (nome,telefone,morada)\nVALUES\n")
InsertVarius(clinicas,file)
file.write("\n")

file.write("INSERT INTO enfermeiro (nif,nome,telefone,morada,nome_clinica)\nVALUES\n")
InsertVarius(Enfermeiros,file)
file.write("\n")

file.write("INSERT INTO medico (nif,nome,telefone,morada,especialidade)\nVALUES\n")
InsertVarius(Medicos,file)
file.write("\n")

file.write("INSERT INTO trabalha (nif,nome,dia_da_semana)\nVALUES\n")
InsertVarius(Trabalhas,file)
file.write("\n")

file.write("INSERT INTO paciente (ssn,nif,nome,telefone,morada,data_nasc)\nVALUES\n")
InsertVarius(Pacientes,file)
file.write("\n")

file.write("INSERT INTO consulta (ssn,nif,nome,data,hora,codigo_sns)\nVALUES\n")
InsertVarius(Consultas,file)
file.write(";")

file.close()