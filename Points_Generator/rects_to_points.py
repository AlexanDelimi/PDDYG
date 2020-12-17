from rectangles_csv_handling import csv_to_rects
import csv
from random import uniform, triangular

def rect_to_points(rect, csv_writer):
    
    for _ in range(int(rect['npoints'])):
        
        if rect['x_distr'] == 'uniform':
            x = uniform(rect['x_min'], rect['x_max'])
        elif rect['x_distr'] == 'triangular':
            mode = float(rect['mode']) if rect['mode'] != "-" else ( rect['x_min'] + rect['x_max'] ) / 2
            x = triangular(rect['x_min'],rect['x_max'], mode)
        
        if rect['y_distr'] == 'uniform':
            y = uniform(rect['y_min'], rect['y_max'])
        elif rect['y_distr'] == 'triangular':
            mode = float(rect['mode']) if rect['mode'] != "-" else ( rect['y_min'] + rect['y_max'] ) / 2
            y = triangular(rect['y_min'],rect['y_max'], mode)

        csv_writer.writerow([x, y])


def create_dataset_from_rects(csv_file, rects):
    with open(csv_file, newline='', mode='w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for rect in rects:
            rect_to_points(rect, csv_writer)


if __name__ == '__main__':
    rects = csv_to_rects('rect_test_npoints.csv')
    csv_file = 'test_points.csv'
    create_dataset_from_rects(csv_file, rects)
    
