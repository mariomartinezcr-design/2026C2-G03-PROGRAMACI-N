import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "María"],
    "Edad": [30, 45, 40, 60],
    "Ciudad": ["Heredia", "Cartago", "Heredia", "Puntarenas"],
}

df = pd.DataFrame(datos)

print("--- Tabla Completa ---")
print(df)

edad_promedio = df["Edad"].mean()
print(f"\nEdad promedio: {edad_promedio} años")


print("\n--- Personas en Heredia ---")
filtro_heredia = df[df["Ciudad"] == "Heredia"]
print(filtro_heredia)
