import requests

BASE = "https://www.ovsicori.una.ac.cr/sistemas/sentidos_map/index.php"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Intentos comunes de parámetros de fecha
intentos = [
    {"tipo": "center", "anio": "2026"},
    {"tipo": "center", "fecha_inicio": "2026-01-01", "fecha_fin": "2026-08-18"},
    {"tipo": "center", "desde": "2026-01-01", "hasta": "2026-08-18"},
    {"tipo": "center", "year": "2026"},
    {"tipo": "center", "ano": "2026"},
]

for params in intentos:
    resp = requests.get(BASE, params=params, headers=headers, timeout=15)
    print("="*60)
    print("Params:", params)
    print("URL final:", resp.url)
    print("Longitud respuesta:", len(resp.text))
    # Contar cuántas filas de datos (tr) tiene
    conteo_tr = resp.text.count("<tr")
    print("Cantidad de <tr>:", conteo_tr)