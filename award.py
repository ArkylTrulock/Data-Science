# Request user inputs their qualifying time
qualifying_time = int(input("Please insert your qualifying time: "))
          
# Variables with their assigned values
within_qualifying_time = "Provincial Colours"
within_five_mins_of_qualifying_time = "Provincial half colours"
within_ten_mins_of_qualifying_time = "Provincial scroll"
more_than_ten_minutes_off_qualifying_time = "No award"

# Time range is between 0 and 100 minutes
if (qualifying_time >= 0) and (qualifying_time <= 100):
    print(f"Your time is {qualifying_time} minte(s)!. Congratulations! You have been awarded the {within_qualifying_time}.")
# Time range is between 101 and 105 minutes
elif (qualifying_time >= 101) and (qualifying_time <= 105):
     print(f"Your time is {qualifying_time} minute(s)!. Congratulations! You have been awarded the {within_five_mins_of_qualifying_time}.")
# Time range is between 106 and 110 minutes
elif (qualifying_time >= 106) and (qualifying_time <= 110):
     print(f"Your time is {qualifying_time} minute(s)!. Congratulations! You have been awarded the {within_ten_mins_of_qualifying_time}.")
# Time range is from 111 minutes and upwards.
elif (qualifying_time >= 111):
     print(f"Your time is {qualifying_time} minute(s)!. Really sorry, better luck next time :(. There is {more_than_ten_minutes_off_qualifying_time} unfortunately.")

else:
      print("Please insert your qualifying time")