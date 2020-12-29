import csv

def drs_to_csv(csv_file, drs):
    csv_columns = ['x_min','x_max','y_min', 'y_max']
    rect_list = []
    for dr in drs:
        rect_list.append(
            {
                'x_min': dr.rect.get_x(),
                'x_max': dr.rect.get_x() + dr.rect.get_width(),
                'y_min': dr.rect.get_y(),
                'y_max': dr.rect.get_y() + dr.rect.get_height()
            }
        )
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for rect in rect_list:
            writer.writerow(rect)


def csv_to_bars(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        bars = []
        for row in reader:
            x_min = float(row['x_min'])
            x_max = float(row['x_max'])
            y_min = float(row['y_min'])
            y_max = float(row['y_max'])
            bars.append(
                {
                    'x': (x_min + x_max) / 2,
                    'height': y_max - y_min,
                    'width': x_max - x_min,
                    'bottom': y_min
                }
            )
    return bars
