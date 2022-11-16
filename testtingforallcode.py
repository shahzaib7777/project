from test import bmi, how_healthy # import the function 'bmi' from the module 'test.py' (no file extension required).

# code to ask user
# ...

# conditional logic to run appropriate functions

# if asked for bmi, run this
user_height = int(input("Please Enter Your height in cm: "))
user_weight = int(input("Now Please enter your weight in kg: "))

the_bmi = bmi(height=user_height, weight=user_weight)
print(f"your bmi is {the_bmi}")
how_healthy(the_bmi)

# else, do something else...
import lets_see