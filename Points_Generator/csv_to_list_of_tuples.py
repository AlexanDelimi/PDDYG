import csv

with open('50_random_numbers.csv') as f:
    for line in csv.reader(f):
        data = [tuple([float(i) for i in line]) for line in csv.reader(f)]

    print(data)