import csv

class Node:
    def __init__(self, id, latitude, longitude, name):
        self.id = id
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.name = name


def import_csv(filename):
    nodes = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            id = row[0]
            latitude = row[1]
            longitude = row[2]
            name = row[3]
            nodes.append(Node(id, latitude, longitude, name))
    return nodes



