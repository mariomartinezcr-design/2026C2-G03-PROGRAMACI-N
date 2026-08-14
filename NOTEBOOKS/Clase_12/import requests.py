import requests
from bs4 import BeautifulSoup

# 1. Definimos la URL de Worldometer para Costa Rica
url = "https://www.worldometers.info/es/poblacion-mundial/poblacion-costa-rica/"

# Es una buena práctica añadir un 'User-Agent' para que el servidor entienda la petición
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

respuesta = requests.get(url, headers=headers)
sopa = BeautifulSoup(respuesta.text, "html.parser")

# 2. Buscamos la tabla dentro del contenedor de clases típico de Worldometer
# Usamos find_all porque la página tiene un par de tablas (histórico, proyecciones, etc.)
tablas = sopa.find_all("table", class_="table")

if tablas:
    # Tomamos la primera tabla (Población histórica)
    tabla_historica = tablas[0]
    
    # 3. Iteramos por las filas de la tabla
    for fila in tabla_historica.find_all("tr"):
        columnas = fila.find_all("td")
        
        # Filtramos para asegurarnos de que la fila tiene datos y no es el encabezado
        if len(columnas) > 0:
            año = columnas[0].text.strip()
            poblacion = columnas[1].text.strip()
            cambio_anual = columnas[2].text.strip()
            poblacion_urbana = columnas[9].text.strip()
            
            print(f"Año: {año} | Población Total: {poblacion} | Crecimiento: {cambio_anual} | Pob. Urbana: {poblacion_urbana}")
else:
    print("No se encontró la tabla en la página.")