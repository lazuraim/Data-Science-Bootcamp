import sys

def print_table(file_path):
    with open(file_path, 'r') as emails, open('employees.tsv', 'a') as employees:
        employees.write("Name\tSurname\tE-mail\n")
        for line in emails:
            name_and_surname = line.split('@')[0]
            name, surname = str(name_and_surname).split('.')
            employees.write(f'{name.capitalize()} \t{surname.capitalize()}\t{line}')



if __name__ == "__main__":
    if len(sys.argv) == 2:
        print_table(sys.argv[1])
    else:
        print("Enter path to the file")