from ds import *
from nodes import *
import csv

# CSV dosyasını okuyup Node listesi döndür
def import_csv(filename):
    nodes = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # başlık satırını atla
        for row in reader:
            id = row[0]
            latitude = row[1]
            longitude = row[2]
            name = row[3]
            nodes.append(Node(id, latitude, longitude, name))
    return nodes

# Stack’i oluştur
stack = Stack()

# CSV’den verileri oku
nodes = import_csv("coordinates.csv")

# Stack’e ekle
for node in nodes:
    stack.push(node)

# Stack’ten çıkar ve yazdır
while True:
    node = stack.pop()
    if node is None:
        break
    print(f"Removed Node: {node.data.id} - {node.data.name}")


