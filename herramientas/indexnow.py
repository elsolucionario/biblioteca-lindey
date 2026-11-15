"""Avisa a Bing y otros buscadores (IndexNow) de las páginas nuevas o modificadas.

Uso en GitHub Actions (ver .github/workflows/publicar.yml):
  python herramientas/indexnow.py lista sitemap_anterior.xml _site/sitemap.xml  -> imprime las URL nuevas o cambiadas (JSON)
  python herramientas/indexnow.py enviar '<json con URLs>'                        -> las envía a api.indexnow.org

No afecta a Google: Google sigue usando el sitemap y Search Console.
"""
import json, sys, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}

def entradas(ruta):
    try:
        raiz = ET.parse(ruta).getroot()
    except Exception:
        return {}
    return {u.findtext("s:loc", namespaces=NS): u.findtext("s:lastmod", default="", namespaces=NS)
            for u in raiz.findall("s:url", NS)}

def clave():
    for f in (RAIZ / "estaticos").glob("*.txt"):
        texto = f.read_text().strip()
        if f.stem == texto:
            return texto
    sys.exit("No hay archivo de clave IndexNow en estaticos/")

def main():
    if sys.argv[1] == "lista":
        antes, ahora = entradas(sys.argv[2]), entradas(sys.argv[3])
        nuevas = [u for u, f in ahora.items() if u not in antes or antes[u] != f]
        print(json.dumps(nuevas[:10000]))
    elif sys.argv[1] == "enviar":
        urls = json.loads(sys.argv[2] or "[]")
        if not urls:
            print("IndexNow: no hay páginas nuevas ni modificadas."); return
        host = urls[0].split("/")[2]; k = clave()
        cuerpo = json.dumps({"host": host, "key": k, "keyLocation": f"https://{host}/{k}.txt", "urlList": urls}).encode()
        pet = urllib.request.Request("https://api.indexnow.org/IndexNow", data=cuerpo,
                                     headers={"Content-Type": "application/json; charset=utf-8"})
        try:
            with urllib.request.urlopen(pet, timeout=30) as r:
                print(f"IndexNow: {len(urls)} URL enviadas (HTTP {r.status}).")
        except urllib.error.HTTPError as e:
            print(f"IndexNow respondió HTTP {e.code}: {e.read()[:300]!r}")  # no detiene la publicación

if __name__ == "__main__":
    main()
