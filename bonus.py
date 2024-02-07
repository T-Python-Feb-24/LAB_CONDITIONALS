weight:float = float(input("Enter your wieght in kilos : "))
height:int = int(input("Enter your height in centimeter : "))
BMI:float = weight / (height/100)**2
print(round(BMI,2))

if BMI >= 25:
    print("You are overwieght you need to work out more and watch your diet.")

if BMI >= 18.5 and BMI < 25:
    print("You are fit & healthy.")
    
if BMI < 18.5:
    print("You are underweight. Watch your health.")

