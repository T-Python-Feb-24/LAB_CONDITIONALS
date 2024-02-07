weight:float = float(input("Enter your wieght in kilos : "))
height:float = float(input("Enter your height cm : "))
BMI:float = weight / height**2

if BMI < 18.5:
    print("You are underweight. Watch your health.")

elif BMI >= 18.5:
    print("You are fit & healthy.")

elif BMI >= 25:
    print("You are overwieght you need to work out more and watch your diet.")