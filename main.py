from tracker import add_energy_data, read_energy_data
from analysis import calculate_average_consumption, calculate_weekly_consumption, calculate_monthly_consumption
from suggestions import provide_suggestions
from visualizer import plot_energy_data

def main():
    while True:
        print("\nEnergy Consumption Tracker")
        print("1. Add Energy Data")
        print("2. View Consumption Data")
        print("3. Analyze Consumption")
        print("4. View Suggestions")
        print("5. Visualize Consumption")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            consumption = float(input("Enter today's energy consumption (kWh): "))
            add_energy_data(consumption)

        elif choice == "2":
            data = read_energy_data()
            for entry in data:
                print(f"Date: {entry['date']}, Consumption: {entry['consumption']} kWh")

        elif choice == "3":
            data = read_energy_data()
            avg_consumption = calculate_average_consumption(data)
            weekly_consumption = calculate_weekly_consumption(data)
            monthly_consumption = calculate_monthly_consumption(data)
            print(f"Average Daily Consumption: {avg_consumption:.2f} kWh")
            print(f"Total Weekly Consumption: {weekly_consumption:.2f} kWh")
            print(f"Total Monthly Consumption: {monthly_consumption:.2f} kWh")

        elif choice == "4":
            data = read_energy_data()
            avg_consumption = calculate_average_consumption(data)
            suggestion = provide_suggestions(avg_consumption)
            print(suggestion)

        elif choice == "5":
            data = read_energy_data()
            plot_energy_data(data)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
