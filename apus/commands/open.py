#!/usr/bin/env python3
import sys
import os
import zipfile
import tarfile
import tempfile
import shutil

if len(sys.argv) < 3:
    print("Use: apus open <archive.apuspack> <destiny_dir>")
    sys.exit(1)

pack = sys.argv[1]
dest = sys.argv[2]

if not os.path.exists(pack):
    print("Error: .apuspack not found:", pack)
    sys.exit(1)

# Carpeta temporal para validar antes de mover
tmp = tempfile.mkdtemp()

def extract_zip(path, dest):
    with zipfile.ZipFile(path, "r") as z:
        z.extractall(dest)
        return z.namelist()

def extract_tar(path, dest):
    with tarfile.open(path, "r:*") as t:
        t.extractall(dest)
        return t.getnames()

# Detectar tipo
ext = pack.lower()

if zipfile.is_zipfile(pack):
    print("Format detected: zip")
    contenido = extract_zip(pack, tmp)

elif tarfile.is_tarfile(pack):
    print("Format detected: tarball")
    contenido = extract_tar(pack, tmp)

else:
    print("Error: not supported format.")
    print("Supported formats: ZIP, TAR, TGZ, TBZ2, TXZ")
    shutil.rmtree(tmp)
    sys.exit(1)

# Validar APUSMARKER
marker_found = False
for root, dirs, files in os.walk(tmp):
    if "APUSMARKER.txt" in files:
        marker_found = True
        break

if not marker_found:
    print("Error: This isn't a real .apuspack (APUSMARKER.txt doesn't exists)")
    shutil.rmtree(tmp)
    sys.exit(1)

print("Validación correcta: APUSMARKER.txt encontrado.")

# Mover contenido al destino
os.makedirs(dest, exist_ok=True)

for item in os.listdir(tmp):
    src = os.path.join(tmp, item)
    dst = os.path.join(dest, item)
    if os.path.isdir(src):
        shutil.move(src, dst)
    else:
        shutil.move(src, dest)

shutil.rmtree(tmp)

print("Paquete extraído correctamente.")
print("Contenido disponible en:")
print(dest)

