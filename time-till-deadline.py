from datetime import datetime

user_input = input("Enter your goal wth a deadline, separated by colon\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

print(input_list)

deadline_date = (datetime.strptime(deadline,"%d.%m.%Y"))

today_date = datetime.today()

#calculate how many days from now until the dealine

time_remaining = deadline_date - today_date
print(time_remaining)

integral_hours_tile = int(time_remaining.total_seconds() /60 /60)
print(f"Dear user, the time reamining for your goal {goal} is {time_remaining.days} days")
print(f"Dear user, the time reamining for your goal {goal} is {time_remaining.total_seconds() /60 /60} hours")
print(f"Dear user, the time reamining for your goal {goal} is {integral_hours_tile} hours")





