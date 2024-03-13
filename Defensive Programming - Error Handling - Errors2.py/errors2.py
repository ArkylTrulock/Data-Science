#animal = Lion
#animal_type = "cub"
#number_of_teeth = 16

# Name error
# Variable animal is not defined. Present Lion as a string "Lion"
animal = "Lion"
animal_type = "Cub"
number_of_teeth = 16

#full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

# Logical and missing paranthesis error
# Define full_spec by presenting variables animal, animal_type & number_of_teeth as {0},{1},{2} (to represent the first, second and third variables).format(variable 1,variable 2, variable 3) 
full_spec=("This is a {0}. It is a {1} and has {2} teeth.".format(animal,animal_type,number_of_teeth))

print(full_spec)