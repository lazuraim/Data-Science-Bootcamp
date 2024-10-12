import sys

def find_name(email: str):
    name_and_surname = email.split('@')[0]
    name = str(name_and_surname).split('.')[0]
    print(f'Dear {name.capitalize()}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        find_name(sys.argv[1])
    else:
        print("Enter email from 'employees.tsv'")