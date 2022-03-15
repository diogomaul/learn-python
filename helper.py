import logging

#Function to conver a number of days to a specific unit set by the user
def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == "hours":        
        return (f"{number_of_days} days are {number_of_days * 24} hours")
    elif conversion_unit == "minutes":
        return (f"{number_of_days} days are {number_of_days * 24 * 60} minutes")
    elif conversion_unit == "seconds":
        return (f"{number_of_days} days are {number_of_days * 24 * 60 * 60} seconds")
    else:
        return "Unsupported unit"

#funtion to validate if the value entry by the user is valid.
def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            caulculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print (caulculated_value)
        elif user_input_number == 0:
            print ("You entered the number 0, nothing to calculate")
        else:
            print ("You entered a negative number, nothing to calculate")
    except ValueError:
        print ("The input value is invalid, please add a integral positive number")

user_message = ("Enter a number of days and conversion unit:\n")