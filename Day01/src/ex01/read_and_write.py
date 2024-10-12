
def parse_csv():
    with open('ds.csv', 'r') as input, open('ds.tsv', 'a') as output:
        for line in input:
            for index, char in enumerate(line):
                if char == ',' and (line[index-1] == '"' or line[index+1] == '"'):
                    char = '\t'
                output.write(char)

if __name__ == "__main__":
    parse_csv()