class Must_read:
    try:
        with open('data.csv', 'r') as file:
            print(file.read())
    except Exception as error_message:
        print(error_message)
    
if __name__ == "__main__":
    mr = Must_read()
    
    