import sys
import os

class Research:
    def __init__(self, filepath):
        self.filepath = filepath
        self.error_message = 'File not found or wrong format'
        self.lines = 0
        self.calc = self.Calculations()

    def file_reader(self, has_reader=True):
        if not Research.check_file(self):
            raise IOError(self.error_message)
        else:
            with open(self.filepath, 'r') as file:
                has_header = Research.check_header(self, file.readline())
                output = []
                for line in file:
                    new_list = line.split(',')
                    new_list = [int(elem) for elem in new_list]
                    output.append(new_list)
                return(output)


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
    
    class Calculations:
        def counts(self, data_from_file):
            heads = 0
            tails = 0
            for head, tail in data_from_file:
                heads += head
                tails += tail
            return(heads, tails)

        def fractions(selv, heads, tails):
            total = heads + tails
            return(heads/total, tails/total)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            r1 = Research(sys.argv[1])
            output = r1.file_reader()
            print(output)
            c1 = r1.calc
            heads, tails = c1.counts(output)
            print(heads, tails)
            percents = c1.fractions(heads, tails)
            print(percents)
        except Exception as error_message:
            print(error_message)
    else:
        print("Enter path to the file")