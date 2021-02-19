''' The functions in this file help us ensure
that the formatted real datasets created by 
downsampling and oversampling the original datasets
are formatted as needed.
'''

import os
import csv
from operator import itemgetter
from pprint import pprint


def formatted_sizes():
    ''' Print the sizes of the formatted real datasets. '''

    size = {}
    filenames = os.listdir( './formatted_CSVs' )
    for name in filenames:
        with open('./formatted_CSVs/' + name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            size[name] = sum(1 for row in reader)
    pprint(size)


def formatted_ranges():
    ''' Print the coordinates range of the formatted real datasets. '''

    filenames = os.listdir( './formatted_CSVs' )
    for name in filenames:
        print(name)
        with open('./formatted_CSVs/' + name, 'r') as csvfile: 
            list_of_tuples = [tuple([float(i) for i in line]) for line in csv.reader(csvfile)]
            xmin = min(list_of_tuples, key=itemgetter(0))[0]
            xmax = max(list_of_tuples, key=itemgetter(0))[0]
            ymin = min(list_of_tuples, key=itemgetter(1))[1]
            ymax = max(list_of_tuples, key=itemgetter(1))[1]
            print('x in ' + str(xmin) + ' - ' + str(xmax))
            print('y in ' + str(ymin) + ' - ' + str(ymax))


def dataset_sizes():
    ''' Print the sizes of the real datasets before formatting them. '''

    for i in range(1, 7):
        print(i)
        filenames = os.listdir( './Internet_Datasets/set_' + str(i) )
        for name in filenames:
            with open('./Internet_Datasets/set_' + str(i) + '/' + name, 'r') as csvfile:
                reader = csv.reader(csvfile)
                print(name, sum(1 for row in reader) )


if __name__ == "__main__":

    # set directory at file location
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    os.chdir(dirname)

    formatted_sizes()
    print('\n\n')
    formatted_ranges()
    print('\n\n')
    dataset_sizes()