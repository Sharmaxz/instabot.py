import csv


def format_csv(csv_file, start_row, column, city, country):
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', encoding='utf8')
        locations = []
        formated_locations = []
        row_count = 0
        for place in csv_reader:
            if row_count >= start_row:
                locations.append(place[column])
                formated_locations.append(f'{place[column]}, {city}, {country}')
            row_count += 1

    return formated_locations
