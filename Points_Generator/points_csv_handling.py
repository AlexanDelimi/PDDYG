import csv
import matplotlib.pyplot as plt


def points_csv_to_list_of_tuples(csv_file):
    with open(csv_file) as f:
        list_of_tuples = [tuple([float(i) for i in line]) for line in csv.reader(f)]
    return list_of_tuples


def visualize_list_of_tuples(list_of_tuples):
    x = [pair[0] for pair in list_of_tuples]
    y = [pair[1] for pair in list_of_tuples]
    plt.scatter(x, y)
    plt.show()


if __name__ == '__main__':
    list_of_tuples = points_csv_to_list_of_tuples('test_points.csv')
    visualize_list_of_tuples(list_of_tuples)