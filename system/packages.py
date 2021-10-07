import os
import subprocess
import sys


def list_packages():
    packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    return [r.decode().split('==')[0] for r in packages.split()]


def install_package(*args, download=True):
    installed_packages = list_packages()

    for package in args:
        if package not in installed_packages:
            print(f"{package} not found...\n")
            if download:
                print(f"{package} is being downloaded...")
                # os.system(f"python -m pip install --upgrade {package}")

        else:
            print(f"{package} is installed.")


