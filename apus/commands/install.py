#!/usr/bin/env python3
import sys
import os
import subprocess

if len(sys.argv) < 2:
    print("Use: apus install <package_directory>")
    sys.exit(1)

root = sys.argv[1]
build = os.path.join(root, "build")

# Validar carpeta build
if not os.path.exists(build):
    print("Error: directory build doesn't exist.")
    print("Ejecuta primero: apus build", root)
    sys.exit(1)

# Prefijo de instalación estándar
prefix = "/usr/local"

print("Installing on:", prefix)

result = subprocess.run([
    "sudo", "cmake", "--install", build, "--prefix", prefix
])

if result.returncode != 0:
    print("Sorry, your install has failed.")
    sys.exit(1)

print("Installation completed.")
print("Binarios instalados en:", prefix)

