#!/usr/bin/env python3
import sys
import os
import subprocess

def run(cmd, args):
    path = os.path.join(os.path.dirname(__file__), "commands", cmd + ".py")
    if not os.path.exists(path):
        print(f"Unknown command: {cmd}")
        return
    subprocess.run(["python3", path] + args)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("APUS - AltusOS package manager.")
        print("Available commands:")
        print("  download")
        print("  open")
        print("  build")
        print("  install")
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]
    run(cmd, args)

