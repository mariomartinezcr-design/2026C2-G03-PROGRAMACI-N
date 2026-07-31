"""Programa principal del proyecto modular BCCR."""

from lectura_datos import cargar_tabla_bccr, mostrar_top_10, resumir_por_tipo_entidad
from limpieza_datos import limpiar_datos

def ejecutar():
    """Cargar los datos y presentar el menú del sistema"""
    datos_crudos = cargar_tabla_bccr()
    datos = limpiar_datos(datos_crudos)
    
    while True:
        print("\nPROYECTO ANALISIS BCCR")
        print("1. Mostrar primeras 10 entidades limpias.")
        print("2. Promedio por tipo de entidad.")
        print("3. Mostrar entidades financieras con diferencial mayor al promedio.")
        print("4. Mostrar lista de entidades y exportar CSV.")
        print("5. Graficar")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":                                               
            print(mostrar_top_10(datos))
        elif opcion == "2":
            promedios = resumir_por_tipo_entidad(datos)
            print(f"Promedio general del diferencial: {promedios[0]:.2f}")
            print("Promedios por tipo de entidad:")
            print(promedios[1]).to_string(index=True)      
        elif opcion == "3":
            print("Entidades con diferencial mayor al promedio:")
            entidades_altas = filtrar_diferencial_alto(datos)
            print(mostrar_top_10(entidades_altas))
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Graficando...")
        elif opcion == "6":
            print("Análisis finalizado")
            input("Presione enter para salir...")
            break
        else:
            print("Opción invalidad. escriba un número del 1 al 6")
        input("\nPresione enter para continuar...\n")
            
if __name__ == "__main__":
    ejecutar()
