print("BMI Calculater System")

#Wieght and height from the user
wieght:str = float (input("Enter your wieght in kg: "))
height:str = float(input("Enter your height in cm: "))

#calculate the BMI 
bmi:float = round(wieght / ((height/100)**2), 2)

print ("Your BMI is {}".format(bmi))

#Check BMI status
if bmi >= 40.0:
    print("Status: You are OBESE you need to check the doctor.")
elif bmi >= 25.0 and bmi <= 39.9:
    print("Status: You are OVERWIEGHT you need to work out more and watch your diet.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Status: You are NORMAL fit & healthy.")
else:
    print("Status: You are UNDERWEIGHT. Watch your health.")