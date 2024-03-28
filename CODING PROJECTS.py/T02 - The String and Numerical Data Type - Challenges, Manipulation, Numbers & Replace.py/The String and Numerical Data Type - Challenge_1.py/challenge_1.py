# Imported math function sqrt has been imported.
from cmath import sqrt
import math

# Request user to input length of three sides of the triangle side_1,side_2 & side_3.
side_1 = float(input("Please insert length: "))
side_2 = float(input("Please insert length: "))
side_3 = float(input("Please insert length: "))

# Divide the sum of the length of the sides by 2 to calculate s.
s=(side_1+side_2+side_3)/2

#Calculate the area of the triangle as per the formula below using square root which is sqrt. 
area=sqrt(s*(s-side_1)*(s-side_2)*(s-side_3))

answer = f"The final answer to our question is {area}"
print(answer)


