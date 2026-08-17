#!/usr/bin/env python3
import os
import urllib.request

cache = os.path.expanduser("~/.apus/cache")
os.makedirs(cache, exist_ok=True)

print("Introduce the name of the repo of Altus-Project-User-Software:")
print("https://github.com/Altus-Project-User-Software/__________")
repo = input("> ")

print("Introduce el release tag (v1.0, v2.3, stable):")
tag = input("> ")

print("Introduce the name of the .apuspack in that release.:")
pack = input("> ")

url = f"https://github.com/Altus-Project-User-Software/{repo}/releases/download/{tag}/{pack}"

print("Downloading from:")
print(url)

dest = os.path.join(cache, pack)

try:
    urllib.request.urlretrieve(url, dest)
    print(f"Saved on {dest}")
except Exception as e:
    print("Download error. Try another apuspack.:", e)

