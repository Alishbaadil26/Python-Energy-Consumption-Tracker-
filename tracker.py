import csv
from datetime import datetime

def add_energy_data(consumption):
    with open('data/energy_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        date = datetime.now().strftime('%Y-%m-%d')
        writer.writerow([date, consumption])
        print(f"Added {consumption} kWh for {date}")

def read_energy_data():
    data = []
    with open('data/energy_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append({"date": row[0], "consumption": float(row[1])})
    return data
