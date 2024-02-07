# write a program that Calculates the BMI 
#(body mass index) of the user:

weight = input("Please enter your weight : ")
height = input("Please enter your height : ")

BMI = weight/height**2

if BMI <= 29.9:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI <= 24.9:
    print("You are fit & healthy.")
elif BMI <= 18.5:
    print("You are underweight. Watch your health.")