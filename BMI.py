#Ask the user to provide his wieght
user_weight:str = float(input("Please enter your weight in kilograms: "))

#Ask the user to provide his height
user_height:str = float(input("Please enter your height in cm: "))

#Convert metrics
from_cm_to_m:float = user_height/100

# Calculate the BMI
BMI = user_weight / (from_cm_to_m**2)
print("Your BMI is: ", BMI)

# Categorize the BMI value
if BMI > 1:
    if BMI <= 16:
        print("You are underweight. Watch your health")
    elif BMI <= 25:
        print("You are fit & healthy")
    elif BMI > 25:
        print("You are overwieght you need to work out more and watch your diet")
else:
    print("ERROR. Enter valid details!!")

