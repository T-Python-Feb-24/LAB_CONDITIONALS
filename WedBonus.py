### write a program that Calculates the BMI (body mass index) of the user:
''''
- Ask the user to provide his wieght.
- Ask the user to provide hi height.
- print the BMI for the user.
- using conditionals tell the user that either :
- - You are overwieght you need to work out more and watch your diet.
- - You are fit & healthy.
- - You are underweight. Watch your health.
'''
weight = float(input("Enter your weight in kilograms: "))

height = float(input("Enter your height in meters: "))

bmi = weight / (height** 2)

print("Your BMI is:", bmi)

if bmi > 30:

    print("You are overwieght. You need to work out more and watch your diet.")

elif bmi >= 19.5:
    
    print("You are fit and healthy.")

else:
    print("You are underweight. Watch your health.")