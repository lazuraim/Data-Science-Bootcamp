import sys
from random import randint
import logging
import requests

class Research:
    def __init__(self, filepath):
        self.filepath = filepath
        self.error_message = 'File not found or wrong format'
        self.lines = 0
        self.calc = self.Calculations()

    def file_reader(self, has_reader=True):
        if not Research.check_file(self):
            logging.debug(f'Could not open/read file: {self.filepath} because of {self.error_message}')
            raise IOError(self.error_message)
        else:
            logging.debug('Reading file')
            with open(self.filepath, 'r') as file:
                has_header = Research.check_header(self, file.readline())
                output = []
                for line in file:
                    new_list = line.split(',')
                    new_list = [int(elem) for elem in new_list]
                    output.append(new_list)
                return(output)
    
    def check_file(self):
        logging.debug('Checking format of the file')
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
        logging.debug('Checking header')
        if header != 'head,tail\n':
            self.error_message = 'No header or empty file'
            return False
        return True
    
    def check_delimiter(self, line):
        logging.debug('Checking delimiters')
        if line[1] != ',':
            self.error_message = 'Wrong delimiter'
            return False
        return True
    
    def check_content(self, line):
        logging.debug('Checking format of lines')
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

    def webhook(self, url, user_id, message):
        requests.get(f"{url}?chat_id={user_id}&text={message}")
    
    class Calculations:
        def __init__(self):  
            self.heads = 0
            self.tails = 0

        def counts(self, data_from_file):
            logging.debug('Calculating the counts of heads and tails')
            for head, tail in data_from_file:
                self.heads += head
                self.tails += tail
            return(self.heads, self.tails)

        def fractions(self):
            logging.debug('Calculating the percentage of heads and tails')
            total = self.heads + self.tails
            head_percent = self.heads/total
            tail_percent = self.tails/total
            return(head_percent, tail_percent)
    

class Analytics(Research.Calculations):
    def predict_random(self, num_of_predictions):
        logging.debug('Predicting observations of heads and tails')
        list_of_lists = []
        for i in range(0, num_of_predictions):
            if randint(0, 1) == 1:
                list_of_lists.append([1,0])
            else:
                list_of_lists.append([0,1])
        return(list_of_lists)
    
    def count_in_prediction(self, list_of_lists):
        logging.debug('Counting heads and tails in prediction')
        heads = 0
        tails = 0
        for head, tail in list_of_lists:
            heads += head
            tails += tail
        return heads, tails
    
    def predict_last(self, output):
        logging.debug('Defining the last item of the data from file_reader()')
        return output[-1]
    

    def save_file(self, data, filename, extension='txt'):
        logging.debug('Saving report file')
        with open(f'{filename}.{extension}', 'w') as new_file:
            new_file.write(data)
