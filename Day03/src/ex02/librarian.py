import sys
import os
import subprocess


def install_modules():
    subprocess.call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    with open('new_requirements.txt', 'w') as file:
        subprocess.call(['pip', 'freeze'], stdout=file)

if __name__=='__main__':
    venv = os.getenv('VIRTUAL_ENV')
    if not venv:
        print("There is no activated virtual env")
        exit(1)
    if venv.endswith('scabberr'):
        install_modules()
    else:
        raise Exception("Wrong virtual env")
