import requests
from bs4 import BeautifulSoup

url = "https://worldstats.io/rankings/oldest-population"

# Simular un navegador con User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/115.0.0.0 Safari/537.36"
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
  soup = BeautifulSoup(respuesta.text, "html.parser")

  # Ejemplo genérico: buscar filas de una tabla en la página
  # Nota: debes inspeccionar el HTML real de la web para ajustar las etiquetas o clases
  filas = soup.find_all("tr")

  for fila in filas:
    columnas = fila.find_all("td")
    datos = [col.text.strip() for col in columnas]
    if datos:
      print(datos)
else:
  print("Error al acceder a la página:", response.status_code)

