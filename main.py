#import helper
#from helper import *
from helper import validate_and_execute, user_message


import os
print(os.name)

#While function to keep the program running and asking for more numbers to convert
user_input = ""
while user_input != "exit":
    user_input = input(user_message)
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        
    validate_and_execute(days_and_unit_dictionary)


#END OF CODE
