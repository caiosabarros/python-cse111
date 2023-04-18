import math 

width = int(input("What' the width of the tire in mm?"))  
aspect_ratio = int(input("What's the aspect ratio of the tire?"))
diameter = int(input("What's the diameter of the wheel in inches?"))

#Perform calcuclations
volume = ((math.pi) * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000 

print(f"The approximate volume is {volume:.2f} liters")



