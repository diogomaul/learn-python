
to_unit = 24
unit_name = "hours"

def days_to_units(number_of_days):
    return (f"{number_of_days} days are {number_of_days * to_unit} {unit_name}")

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            caulculated_value = days_to_units(user_input_number)
            print (caulculated_value)
        elif user_input_number == 0:
            print ("You entered the number 0, nothing to calculate")
        else:
            print ("You entered a negative number, nothing to calculate")
    except ValueError:
        print ("The input value is invalid, please add a integral positive number")

user_input = ""
while user_input != "exit":
    user_input = input("Enter a number of days in a comma separate list to be converted to hours\n")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days_element in user_input.split(","):
        validate_and_execute()
