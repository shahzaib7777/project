#If your BMI is less than 18.5, it falls within the underweight range.
#If your BMI is 18.5 to <25, it falls within the healthy weight range.
#If your BMI is 25.0 to <30, it falls within the overweight range.
#If your BMI is 30.0 or higher, it falls within the obesity range.

print(True)

def how_healthy(the_bmi):
    if the_bmi <= 18:
        print("your underwqeight lad.")
    elif the_bmi <= 25: 
        print('your healthy')     
    elif the_bmi <= 29:
        print("You are over weight.")
    elif the_bmi <= 34:
        print("You are severely over weight.")
    elif the_bmi <= 39:
        print("You are obese.")
    else:
        print("You are very obese.")
        

def bmi(weight, height):
    return weight / (height/100)**2


 
