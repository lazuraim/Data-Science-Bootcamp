import sys
import os

class Research:
    def __init__(self, filepath):
        self.filepath = filepath
        self.error_message = 'File not found or wrong format'
        self.lines = 0

    def file_reader(self):
        if not Research.check_file(self):
            raise IOError(self.error_message)
        else:
            with open(self.filepath, 'r') as file:
                return(file.read())
                
    def check_file(self):
            with open(self.filepath, 'r') as file:
                if not Research.check_header(self, file.readline()):
                    return False
                for line in file:
                    if len(line) < 3 and self.lines == 0:
                        self.error_message = 'Empty file or wrong format'
                        return False
                    
                    if not Research.check_delimiter(self, line) or \
                       not Research.check_content(self, line):
                        return False
                    self.lines += 1

                if self.lines == 0:
                    self.error_message = 'Empty file'
                    return False
                return True

    def check_header(self, header):
        if header != 'head,tail\n':
            self.error_message = 'No header or empty file'
            return False
        return True
    
    def check_delimiter(self, line):
        if line[1] != ',':
            self.error_message = 'Wrong delimiter'
            return False
        return True
    
    def check_content(self, line):
        line = line.split(',')
        line = [int(elem) for elem in line]
        head, tail = line
        if head == tail:
            self.error_message = 'Head and tails are equal'
            return False
        if head not in (0, 1) or \
                            tail not in (0, 1):
            self.error_message = 'Arguments are not in (0, 1)'
            return False
        return True

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            r1 = Research(sys.argv[1])
            print(r1.file_reader())
        except Exception as error_message:
            print(f"{error_message}")
        
    else:
        print("Enter path to one csv file")