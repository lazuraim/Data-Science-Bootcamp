class Research:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            return(file.read())

if __name__ == "__main__":
    try:
        r1 = Research()
        print(r1.file_reader())
    except Exception as error_message:
        print(error_message)