import csv

from serialization.consts import CSV_FILE

if __name__ == '__main__':
    with open(CSV_FILE, 'a') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Anna Kowalska", 2500])
