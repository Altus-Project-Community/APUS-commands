#!/usr/bin/env python3
import sys
import os
import subprocess

if len(sys.argv) < 2:
    print("Use: apus build <package_dir>")
    sys.exit(1)

root = sys.argv[1]

if not os.path.exists(root):
    print("Error: dir not found:", root)
    sys.exit(1)

# CMakeLists SOLO en la raíz
cmakelists = os.path.join(root, "CMakeLists.txt")

if not os.path.exists(cmakelists):
    print("Error: no se encontró CMakeLists.txt en la raíz del paquete.")
    print("APUS BUILD solo usa el CMakeLists.txt del root.")
    sys.exit(1)

# Carpeta build
build = os.path.join(root, "build")
os.makedirs(build, exist_ok=True)

print("Configuring with CMake, probably soon will move to Ninja")
result = subprocess.run([
    "cmake", "-S", root, "-B", build,
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5"
])

if result.returncode != 0:
    print("Error: CMake no pudo configurar el proyecto.")
    sys.exit(1)

print("Compiling...")
result = subprocess.run(["cmake", "--build", build])

if result.returncode != 0:
    print("Error: failed compilation.")
    sys.exit(1)

print("Compilation completed.")
print("The bin are on:", build)

