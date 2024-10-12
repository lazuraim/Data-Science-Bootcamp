import os

if __name__=='__main__':
    venv = os.environ.get('VIRTUAL_ENV')
    if venv:
        print(f"Your current virtual env is {venv}")
    else:
        print("There is no activated virtual env")
