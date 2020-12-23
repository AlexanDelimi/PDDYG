import csv
from random import uniform, randint

MAX = 100
MIN = -100

def decipher_bounds(**kwargs):
    keys = kwargs.keys()
    
    x_min = MIN 
    if 'x_min' in keys:
        x_min = kwargs['x_min']
    
    x_max = MAX
    if 'x_max' in keys:
        x_max = kwargs['x_max']
    
    y_min = MIN
    if 'y_min' in keys:
        y_min = kwargs['y_min']
    
    y_max = MAX
    if 'y_max' in keys:
        y_max = kwargs['y_max']
    
    # check order consistency and swap to fix it
    if x_min > x_max:
        x_min, x_max = x_max, x_min
    if y_min > y_max:
        y_min, y_max = y_max, y_min

    return x_min, x_max, y_min, y_max


def decipher_coordinates(x_min, x_max, y_min, y_max):

    # check longitude and latitude in legal bounds
    x_min = -180 if x_min < -180 else x_min
    x_max = 180 if x_max > 180 else x_max
    y_min = -90 if y_min < -90 else y_min
    y_max = 90 if y_max > 90 else y_max

    return x_min, x_max, y_min, y_max


def generate_coordinates(**kwargs):

    x_min, x_max, y_min, y_max = decipher_bounds(**kwargs)
    x_min, x_max, y_min, y_max = decipher_coordinates(x_min, x_max, y_min, y_max)

    longitude = uniform(x_min, x_max)
    longitude = "{:.7f}".format(longitude)

    latitude = uniform(y_min, y_max)
    latitude = "{:.7f}".format(latitude)

    return longitude, latitude


def generate_floats_tuple(**kwargs):

    x_min, x_max, y_min, y_max = decipher_bounds(**kwargs)
    x = uniform(x_min, x_max)
    y = uniform(y_min, y_max)

    return x, y


def generate_integers_tuple(**kwargs):

    x_min, x_max, y_min, y_max = decipher_bounds(**kwargs)
    x = randint(x_min, x_max)
    y = randint(y_min, y_max)

    return x, y


def create_dataset(file_name, tuples_number, generator_function, **kwargs):
    with open(file_name, newline='', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for _ in range(tuples_number):
            x, y = generator_function(**kwargs)
            csv_writer.writerow([x, y])


def main():
    create_dataset('asgf.csv', 10, generate_coordinates)

if __name__ == '__main__':
    main()


# uniform() and randint() produce uniform distributions for real and integer numbers respectively
# 
# 2D Inverse Transform Sampling
# https://medium.com/analytics-vidhya/generating-simulated-data-points-that-follow-a-give-probability-density-function-678a50b467fa 
# 
# give each rectangle a distribution per dimension
# uniform and gaussian distributions as choices
# use rectangles to approximate every distribution pattern
# search for papers on the weaknesses of each tree