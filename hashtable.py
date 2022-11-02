import csv
data = []
with open('data.csv', 'w') as f:
    for line in f:
        token = line.split(',')
        name = token[0]
        price = float(token[1])
        data.append([name, price])
        
