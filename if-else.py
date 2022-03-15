
to_unit = 24
unit_name = "hours"

def days_to_units(number_of_days):
    return (f"{number_of_days} days are {number_of_days * to_unit} {unit_name}")

def validate_and_execute():
    if user_input.isdigit():

        user_input_number = int(user_input)
        if user_input_number > 0:
            caulculated_value = days_to_units(user_input_number)
            print (caulculated_value)
        elif user_input_number == 0:
            print ("You entered the number 0, nothing to calculate")
    else:
        print ("The input value is invalid, please add a integral positive number")


user_input = input("Enter a number of days to be converted to hours\n")
validate_and_execute()



