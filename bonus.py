#Ask the user to provide his wieght.
wieght=float(input("Enter your wieght: "))

#Ask the user to provide height.
height=float(input("Enter your height: "))

#Convert Meter to Centimeter
height= height/100


#print the BMI for the user.
bmi=wieght/height**2
print(f"your BMI is:{round(bmi,2)}")

#using conditionals tell the user that either :

if bmi>=25:
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi>=18.5 and bmi<=25:
    print("You are fit & healthy.")
elif bmi<18.5:
    print("You are underweight. Watch your health.")