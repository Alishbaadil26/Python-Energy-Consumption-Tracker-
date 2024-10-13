def calculate_total_consumption(data):
    return sum(entry['consumption'] for entry in data)

def calculate_average_consumption(data):
    return calculate_total_consumption(data) / len(data)

def calculate_weekly_consumption(data):
    return calculate_total_consumption(data[-7:])

def calculate_monthly_consumption(data):
    return calculate_total_consumption(data[-30:])
