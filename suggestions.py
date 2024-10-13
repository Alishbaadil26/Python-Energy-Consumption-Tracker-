def provide_suggestions(average_consumption):
    if average_consumption > 20:
        return "Your average daily consumption is high. Consider switching to energy-efficient appliances."
    elif average_consumption > 10:
        return "You have moderate consumption. Reducing appliance usage during peak hours can help save energy."
    else:
        return "Your energy consumption is low. Keep up the good work!"
