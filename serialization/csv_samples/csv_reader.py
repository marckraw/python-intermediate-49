import csv

from serialization.consts import CSV_FILE

if __name__ == '__main__':

    with open(CSV_FILE) as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for row in reader:
            print(row)
