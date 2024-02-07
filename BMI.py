# Ask the user to provide his wieght.
# Ask the user to provide hi height.
# print the BMI for the user.
'''
using conditionals tell the user that either :
  - You are overwieght you need to work out more and watch your diet.
  - You are fit & healthy.
  - You are underweight. Watch your health.
'''

height = float(input("Your Height (cm): "))
weight = float(input("Your Weight (kg): "))

BMI = weight / (height/100)**2
print("\nBMI: ", round(BMI, 2))

if BMI < 18.5:
    print("You are underweight. watch your health.")
elif BMI >= 18.5 and BMI <= 25:
    print("You are fit & healthy.")
else:
    print("You are overweight. you need to work out more and watch your diet.")
