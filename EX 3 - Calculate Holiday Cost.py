
import time

print("Welcome to Africa Airlines")
print("Please select your destination from the list below:\n ")

capital_name = ["abuja","bissau","cairo","dakar","djibouti city","freetown","gaborone","harare","juba"]
flight_price = {"abuja":1000,"bissau":950,"cairo":645,"dakar":868,"djibouti city":755,"freetown":535,"gaborone":855,"harare":655,"juba":755}
hotel_price_per_night = {"abuja":500,"bissau":510,"cairo":520,"dakar":530,"djibouti city":540,"freetown":535,"gaborone":525,"harare":510,"juba":590}
car_rental_price_per_day = {"abuja":30,"bissau":40,"cairo":50,"dakar":60,"djibouti city":65,"freetown":45,"gaborone":35,"harare":25,"juba":15}

# The names in the capital_name list are printed first giving the user choices to select to proceed with the program.
for city in capital_name:
    print(city)

# Function returns the plane cost
def plane_cost(flight_price,city_flights):
    total_flight_cost = flight_price[city_flights]
    return total_flight_cost 

# Function returns the hotel cost
def hotel_cost(hotel_price_per_night,num_nights):
    total_hotel_cost = hotel_price_per_night[city_flights] * num_nights
    return total_hotel_cost

# Function returns the car rental cost
def car_rental(car_rental_price_per_day,rental_days):
    total_rental_cost = car_rental_price_per_day[city_flights] * rental_days
    return total_rental_cost

# Function returns the holiday cost
def holiday_cost(total_flight_cost,total_hotel_cost,total_rental_cost):
    total_holiday_cost = total_flight_cost + total_hotel_cost + total_rental_cost
    return total_holiday_cost

while True:
    # If the condition is evaluated to be TRUE the block of code below is executed. The proceed and total_flight cost program is activated.
    city_flights = input("Please enter your destination of choice:\t").lower()
    if city_flights in capital_name:
     print(f"Great! Your destination of choice is: {city_flights}")
     print("-------------Please wait---------------")
     time.sleep(2)

    else:
       # If the condition has been evaluated to be FALSE the block of code below is executed.
       print("Invalid destination has been entered!")
       print("Please enter choose destination from the list above and enter to proceed.")
       # The the loop continues/restarts. We restart the city_flights program.
       continue
    
    # Initialise total_flight_cost to 0
    total_flight_cost = 0

    proceed = input("Do you wish to proceed with the flight cost evaluation? Y/N:\t").lower()
    if proceed=="y":
        total_flight_cost = plane_cost(flight_price,city_flights)
        # If the condition is evaluated to be TRUE the block of code below is executed. The num_nights program is activated.
        print("\nYou chose to proceed with the flight cost evaluation.")
        print(f"The cost of the flight to {city_flights} will be:\t £{total_flight_cost}")
    
    elif proceed == "n":
        # If the first condition is evaluated to be FALSE the block of code below is executed. The num_nights program is activated.
        print("\nYou chose not proceed with the flight cost evaluation.")
        print("-----------------Processing order---------------------------")
        #break # Exit the loop. The proceed program terminates and num_nights program is not activated.

    else:
         # If BOTH conditions are evaluated to be FALSE the block of code below is executed.
         print("Please type Y or N to proceed!")
         print("If you have any further queries, please do not hesitate to contact our customer service department @africa-airlines.afr\n")
         # The loop continues. The proceed program restarts.
         continue


    # Initialise num_nights to 0
    num_nights = 0
    # Initialise total_hotel_cost to 0
    total_hotel_cost = 0

    while True:
        try:
           # If the condition is evaluated to be TRUE the block of code below is executed.
           num_nights = int(input("\nHow many nights will you be staying?: \t")) 
           print(f"Great! it has been confirmed you will be staying for: {num_nights} nights.")
           print("-----------------Processing order---------------------------")
           time.sleep(2)

           # If there is a numerical error the block of code below will be executed.
        except ValueError:
            print("\nInvalid numerical value has been entered.")
            print("---Please enter numerical value to proceed---")
            time.sleep(2)
            # The loop continues/restarts. The num_nights program restarts.
            continue  

        hotel_cost_evaluation = input("Do you wish to proceed with hotel cost evaluation? Y/N:\t").lower()
        if hotel_cost_evaluation == "y":
            # If the condition is evaluated to be TRUE the block of code below is executed.
            total_hotel_cost = hotel_cost(hotel_price_per_night,num_nights)
            print("\nYou chose to proceed with the hotel cost evaluation.")
            print(f"The hotel cost for {num_nights} nights in {city_flights} will be:\t £{total_hotel_cost}.")
            # Exit loop. The rental_days program is activated.
            break

        elif hotel_cost_evaluation == "n":
        # If the first condition is evaluated to be FALSE the block of code below is executed. 
         print("\nYou chose not proceed with the hotel cost evaluation.")
         print("-----------------Processing order---------------------------")
         # Exit the loop. The rental_days program is activated.
         break 
       
        else:
            # If BOTH conditions has been evaluated to be FALSE, the block of code below is executed.
            print("\nPlease type Y or N to proceed!")
            print("If you have any further queries, please do not hesitate to contact our customer service department @africa-airlines.afr\n")
            # The loop continues/restarts. The hotel_cost_evaluation program restarts.
            continue
        
    # Initialise rental_days to 0
    rental_days = 0
    # Initialise total_rental_cost to 0
    total_rental_cost = 0

    while True:    
        try:
            # If the condition is evaluated to be TRUE the block of code below is executed.
            rental_days = int(input("\nHow many days would you like to rent a car?: \t"))
            print(f"It has been confirmed you will be renting the car for: {rental_days} days.")
            print("-----------------Processing order---------------------------")
            time.sleep(2)

        # If there is a numerical error the block of code below will be executed.
        except ValueError:
            print("\nInvalid numerical value has been entered.")
            print("---Please enter numerical value to proceed---")
            time.sleep(2)
            # The loop continues. The rental_days program restarts.
            continue
            #break # Exit the loop. The rental_days program terminates, car_rental_cost_evaluation and total_holiday_cost programs are not activated.

        car_rental_cost_evaluation = input("Do you wish to proceed with the car rental cost evaluation? Y/N:\t").lower()
        if car_rental_cost_evaluation == "y":
        # If the condition is evaluated to be TRUE the block of code below is executed. The total_holiday_cost program is activated.
         total_rental_cost = car_rental(car_rental_price_per_day,rental_days)
         print("\nYou chose to proceed with the car rental cost evaluation.")
         print(f"The car rental cost for renting a car for {rental_days} days will be:\t £{total_rental_cost}")
         time.sleep(2)
         #break # Exit the loop. The  car_rental_cost_evaluation terminates and total_holiday_cost programs are not activated.

        elif car_rental_cost_evaluation == "n":
        # If the first condition is evaluated to be FALSE the block of code below is executed. The total_holiday_cost program is activated.
         print("\nYou chose not proceed with the car rental cost evaluation.")
         print("-----------------Processing order---------------------------")
         time.sleep(2)
         #break # Exit the loop. The  car_rental_cost_evaluation terminates and total_holiday_cost programs are not activated.

        else:
         # If BOTH conditions are evaluated to be FALSE the block of code below is executed.
         print("Please type Y or N to proceed!")
         print("If you have any further queries, please do not hesitate to contact our customer service department @africa-airlines.afr\n")
         # The loop continues. The car_rental_cost_evaluation program restarts.
         continue
         
        # We calculate the total_holiday_cost (Grand Total Cost Of The Holiday) as per the formula below.
        total_holiday_cost = holiday_cost(total_flight_cost,total_hotel_cost,total_rental_cost)
        print(f"\nFlight Cost: £{total_flight_cost}| Hotel Cost: £{total_hotel_cost}| Car Rental Cost: £{total_rental_cost}\nTotal Holiday Cost: £{total_holiday_cost}")
        print("On behalf of Africa Airlines, we wanted to say thank you for your purchase.")
        print("If you have any questions or suggestions please email: vernyuyyenwomolo@gmail.com")
        # Exit the loop. The program restarts for the beginning.
        break


             
         




