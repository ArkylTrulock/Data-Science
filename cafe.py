from cmath import sqrt
import math
import copy

# Notes - Data types, python dictionary, looking at lists
items = ['bread','ham','cheese','tomato','olive oil']

stock = {'bread':25,
         'ham':20,
         'cheese':15,
         'tomato':10,
         'olive oil':5
         }

price = {'bread':10,
         'ham':8,
         'cheese':6,
         'tomato':4,
         'olive oil':2 
         }

# Initialise out total price to 0.
item_value = 0

# for loop is used to iterate over our iterable object in this case 'items' variable containing the elements/values which are the same as 'key' names
# in the stock and price dictionaries. The dummy variable 'item' in the for loop can be any letter that MUST be used in our indented code below
for item in items:

    
    # stock[item] * price[item] - The variable 'item' and its correponding 'key' and 'value' in the stock dictionary and price dictionary.
    # We calculate the final 'item_value' by adding the initialised 'item_value' [0.00] + stock[item] * price[item]
    item_value = item_value + stock[item] * price[item]

print(f"The cost of our items {items} is: £{item_value}")
print("Thank you for your business!")
