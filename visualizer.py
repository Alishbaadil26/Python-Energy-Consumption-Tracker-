import matplotlib.pyplot as plt

def plot_energy_data(data):
    dates = [entry['date'] for entry in data]
    consumption = [entry['consumption'] for entry in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, consumption, marker='o')
    plt.title("Daily Energy Consumption")
    plt.xlabel("Date")
    plt.ylabel("Energy (kWh)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
