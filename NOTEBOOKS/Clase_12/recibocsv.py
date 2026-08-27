import pandas as pd

# Ruta del archivo
ruta = r"c:\Users\Usuario\Documents\GitHub\2026C2-G03-PROGRAMACIÓN\NOTEBOOKS\Clase_12\nacimientos_defunciones.csv"

# Leer CSV
df = pd.read_csv(ruta)

# Ver primeras filas
print(df.head())

# Ver información general
print(df.info())

# Estadísticas rápidas
print(df.describe())