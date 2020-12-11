from random import uniform, random, randint
import csv

class Coordinates:
    def __init__(self):
        self.longitude =uniform(-180, 180)
        self.latitude =  uniform(-90, 90)

    def print(self):
        print("Longitude = ",self.longitude, ", Latitude = ",self.latitude)


class Tuples:
    def __init__(self,boundx1,boundx2,boundy1,boundy2):
        self.longitude = uniform(boundx1, boundx2)
        self.latitude = uniform(boundy1, boundy2)


class Integers:
    def __init__(self,boundx1,boundx2,boundy1,boundy2):
        self.longitude = randint(boundx1, boundx2)
        self.latitude = randint(boundy1, boundy2)


def printcsv (lists, filename):

        with open(filename, newline='', mode='w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for x in lists:
                csvwriter.writerow([x.longitude, x.latitude])


def main():
    print("Choose 1 for Coordinates")
    print("Choose 2 to pick your own range for floats")
    print("Choose 3 to pick your own range for integers")
    print("Choose anything else to exit")

    mode = input('Your Choice: ')
    if mode == "1":
        number = input('Give me how many coordinates you want')
        filename = "_coordinates.csv"
        # number=5
        try:
            filename = number + filename
            number = int(number)
            lists = []
            for i in range(number):
                lists.append(Coordinates())
            for y in range(number):
                #lists.__getitem__(y).print()
                printcsv(lists, filename)
        except ValueError:
            print("Invalid number")
    elif mode == "2":
        filename = "_random_numbers.csv"
        memberx1 = input('Give me the lower bound of x axis')
        memberx2 = input('Give me the upper bound of x axis')
        membery1 = input('Give me the lower bound of y axis')
        membery2 = input('Give me the upper bound of y axis')
        number = input('Give me how many tuples you want')
        try:
            filename = number + filename
            number = int(number)
            memberx1 = int(memberx1)
            memberx2 = int(memberx2)
            membery2 = int(membery2)
            membery1 = int(membery1)
            lists = []
            for i in range(number):
                lists.append(Tuples(memberx1, memberx2, membery1, membery2))
            for y in range(number):
                #lists.__getitem__(y).print()
                printcsv(lists, filename)
        except ValueError:
            print("Invalid number")
    elif mode == "3":
        filename = "_random_integers.csv"
        memberx1 = input('Give me the lower bound of x axis')
        memberx2 = input('Give me the upper bound of x axis')
        membery1 = input('Give me the lower bound of y axis')
        membery2 = input('Give me the upper bound of y axis')
        number = input('Give me how many tuples you want')
        try:
            filename = number + filename
            number = int(number)
            memberx1 = int(memberx1)
            memberx2 = int(memberx2)
            membery2 = int(membery2)
            membery1 = int(membery1)
            lists = []
            for i in range(number):
                lists.append(Integers(memberx1, memberx2, membery1, membery2))
            for y in range(number):
                #lists.__getitem__(y).print()
                printcsv(lists, filename)
        except ValueError:
            print("Invalid number")


if __name__ == "__main__":
    main()
