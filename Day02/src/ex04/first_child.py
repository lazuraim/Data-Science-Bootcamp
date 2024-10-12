import sys
from random import randint

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
        def __init__(self):  
            self.heads = 0
            self.tails = 0

        def counts(self, data_from_file):
            for head, tail in data_from_file:
                self.heads += head
                self.tails += tail
            return(self.heads, self.tails)

        def fractions(self):
            total = self.heads + self.tails
            head_percent = self.heads/total
            tail_percent = self.tails/total
            return(head_percent, tail_percent)
    

class Analytics(Research.Calculations):
    def predict_random(self, num_of_predictions):
        list_of_lists = []
        for i in range(0, num_of_predictions):
            if randint(0, 1) == 1:
                list_of_lists.append([1,0])
            else:
                list_of_lists.append([0,1])
        return(list_of_lists)
    
    def predict_last(self, output):
        return output[-1]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            r1 = Research(sys.argv[1])
            file_content = r1.file_reader()
            print(file_content)

            c1 = r1.calc
            heads, tails = c1.counts(file_content)
            print(heads, tails)
            print(c1.fractions())


            a1 = Analytics()
            print(a1.predict_random(3))
            print(a1.predict_last(file_content))
        except Exception as error_message:
            print(error_message)
    else:
        print("Enter path to the file")
