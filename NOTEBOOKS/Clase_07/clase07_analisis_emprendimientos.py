"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(lista_ventas):
    """Recibo una lista, la sumo y retorno el total"""
    return sum(lista_ventas)

def calcular_promedio(lista_ventas):
    """Retorna el promedio de las ventas de la lista de las ventas"""
    return sum(lista_ventas) / len(lista_ventas)

def calcular_porcentaje(total_ventas,meta):
    """Calcula porcentaje de cumplimineto de la meta"""
    return total_ventas / meta * 100

def calcular_clasificacion(porcentaje_logro):
    """Clasifica el emprendimiento segun procentaje de cumplimiento de meta de ventas"""
    if porcentaje_logro >= 100:
        clasificacion_emprendimiento = "Meta alcanzada, emprendimiento rentable"
    elif porcentaje_logro >= 80:
        clasificacion_emprendimiento = "Observación, no se logro la meta"
    else:
        clasificacion_emprendimiento = "ADVERTENCIA, problemas de rentabilidad. URGE ATENCION"
    return clasificacion_emprendimiento

def imprimir_reporte(reporte):
    """Imprime reporte final de ventas por sede"""
    print("\nREPORTE FINAL")
    print("_ * 60")
    for fila in reporte:
        print(f"Emprendimiento: {fila["nombre"]}".upper())
        print(f"Provincia: {fila["provincia"]}")
        print(f"Tipo: {fila["tipo"]}")
        
        print(f"Total semanal: {fila["total"]:,.2f}")
        print(f"Promedio diario: {fila["promedio"]:,.2f}")
        print(f"Porcentaje cumplimiento: {fila["porcentaje"]:,.2f}%")
        print(f"Estado: {fila["estado"]}")
        print("_ * 60")
    print(f"Cantidad de emprendimientos: {len(reporte)}")


#print("Cantidad de sedes: ", len(sedes))
#print(type(sedes), "vrs", type(sedes[0]))
#print("Datos por sede: ",sedes[0].keys())
#print("\nPrimer emprendimiento", sedes[0]["nombre"])



reporte = []
provincias = set()
#faltan mas variables

for emprendimiento in sedes: 
#emprendimiento = sedes[0]
    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]

    total_emprendimiento = calcular_total(ventas)
    promedio_emprendimiento = calcular_porcentaje(total_emprendimiento, meta)
    promedio_diario = calcular_promedio(ventas)
    clasificacion = calcular_clasificacion(promedio_emprendimiento)
    
    provincias.add(emprendimiento["provincia"])
    
   # print("\nEmprendimiento: ", emprendimiento ["nombre"])
   # print("Total Ventas", total_emprendimiento)
   # print("Porcentaje logro", promedio_emprendimiento)
   # print("Promedio diario", promedio_diario)
   # print("Análisis de emprendimiento: ", clasificacion)
reporte.append(
        {
            "nombre": emprendimiento["nombre"],
            "provincia": emprendimiento["provincia"],
            "tipo": emprendimiento["tipo"],
            "total": total_emprendimiento
            "promedio": promedio_diario
            "porcentaje": promedio_emprendimiento
            "estado": clasificacion 
        }
    )
print(provincias)
