import os
import subprocess
import sys


def list_packages():
    packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    return [r.decode().split('==')[0] for r in packages.split()]


def download_package(package):
    os.system(f"python -m pip install --upgrade {package}")


def check_packages(*args, download=True):
    installed_packages = list_packages()

    for package in args:
        if package not in installed_packages:
            print(f"{package} not found...")
            if download:
                print(f"{package} is being downloaded...\n")
                download_package(package)
                return True
            else:
                print(f"Download set to 'False'... Skipping download\n")
                return False
        else:
            print(f"{package} is installed.")
            return True


