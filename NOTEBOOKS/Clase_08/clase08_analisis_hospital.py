"""Semana 08: analisis basico de pacientes desde JSON.

Complete los requerimientos indicados. El objetivo principal es practicar
ciclos: recorrer una lista de pacientes leida desde JSON y acumular indicadores
simples.
"""

import json

ARCHIVO_DATOS = "NOTEBOOKS\\Clase_08\datos_clinica.json"


def calcular_promedio(suma, cantidad):
    """Retorna el promedio de una suma entre una cantidad."""
    return suma / cantidad


def es_adulto_mayor(edad):
    """Retorna True si la edad corresponde a una persona adulta mayor."""
    return edad >= 60


# REQUERIMIENTO 1:
# Construya aqui la lectura del JSON con el docente.
# Al terminar, la variable pacientes debe tener 15 registros.
with open(ARCHIVO_DATOS,"r", encoding="utf-8") as archivo:
    pacientes = json.load(archivo)



if len(pacientes) == 0:
    print("Primero construya con el docente la lectura del JSON.")
    print("Cuando cargue correctamente, debe mostrar 15 pacientes.")
else:
    print("Cantidad de pacientes:", len(pacientes)) 
    # REQUERIMIENTO 2:
    # Explore el primer paciente y muestre sus llaves y valores.
primer_paciente = pacientes[0]
print("Datos del Paciente: ", primer_paciente.items())
print("Primer Paciente: ", primer_paciente["nombre"])
print("Enfermedades: ", primer_paciente["enfermedades"] )

# 2. Exploracion inicial

#  Variables acumuladoras del analisis.  
suma_edades = 0 
conteo_san_jose = 0 
conteo_mujeres = 0
conteo_hombres = 0 
adultos_mayores =[]
total_diagnosticos = 0
 

    # 4. Ciclo principal
    # Cada vuelta del ciclo representa un paciente del JSON.
for paciente in pacientes:
    nombre = paciente["nombre"]
    edad = paciente["edad"]
    provincia = paciente["provincia"]
    genero = paciente["genero"]
    
    suma_edades += edad
    if provincia == "San Jose":
            conteo_san_jose += 1
            
    if genero == "F":
            conteo_mujeres += 1
            
    if genero == "M":
            conteo_hombres += 1
    
    if es_adulto_mayor(edad):
        adultos_mayores.append(nombre)
        
    total_diagnosticos += len(paciente["enfermedades"])
   

        # 3.5 Si es_adulto_mayor(edad) es True, agregue el nombre
        # a adultos_mayores

        # RETO FINAL OPCIONAL:
        # Cada paciente tiene una lista en paciente["enfermedades"].
        # Guarde esa lista en una variable y sume su cantidad con len().

    # REQUERIMIENTO 4:
    # Calcule la edad_promedio usando calcular_promedio().
   # edad_promedio = 0

   #  Resultados
print("\nRESUMEN BASICO")
print("Edad promedio:", (suma_edades / len(pacientes)))
print("Pacientes de San Jose:", conteo_san_jose)
print("Mujeres:", conteo_mujeres)
print("Hombres:", conteo_hombres)
print("Adultos mayores:", adultos_mayores)

print("Total de diagnósticos:", total_diagnosticos)
    # REQUERIMIENTO 5:
    # Escriba dos conclusiones basadas en los resultados.
   # print("\nCONCLUSIONES")
   # print("Conclusion 1: ______________________________")
    #print("Conclusion 2: ______________________________")
