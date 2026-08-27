import requests

URL = "https://www.ovsicori.una.ac.cr/sistemas/sentidos_map/index.php?tipo=center"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

resp = requests.get(URL, headers=headers, timeout=15)
resp.raise_for_status()

with open("embed_debug.html", "w", encoding="utf-8") as f:
    f.write(resp.text)

print("Guardado embed_debug.html, longitud:", len(resp.text))
print(resp.text[:2000])  # Preview