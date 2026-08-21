# -*- coding: utf-8 -*-
"""Genera dist/artifact.html a partir de index.html.

La version publicada se envuelve automaticamente en su propio <html>/<head>/<body>,
asi que este script quita esas etiquetas y deja el contenido tal cual.
Ejecutar cada vez que se edite index.html y se quiera actualizar la pagina online:

    python publicar.py
"""
import io, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, "index.html"), encoding="utf-8").read()

quitar = ["<!DOCTYPE html>", "<head>", "</head>", "<body>", "</body>", "</html>"]
out = src
for t in quitar:
    out = out.replace(t, "")
out = re.sub(r'<html[^>]*>', '', out)

# En la galeria de artifacts el titulo funciona como nombre, no como titular SEO.
out = re.sub(r'<title>.*?</title>', '<title>Dulce Salado</title>', out, count=1, flags=re.S)

out = re.sub(r'\n{3,}', '\n\n', out).strip() + "\n"

os.makedirs(os.path.join(BASE, "dist"), exist_ok=True)
destino = os.path.join(BASE, "dist", "artifact.html")
io.open(destino, "w", encoding="utf-8", newline="").write(out)
print("dist/artifact.html generado: %.0f KB" % (len(out) / 1024))
