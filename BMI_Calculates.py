wieght:int = float(input("Insert your wieght in kg -> " ))
height:int = float(input("Insert your height in cm -> " ))
height = height/100

bmi = wieght / (height ** 2) 

print("-"*20)

print(f"your BMI =>{bmi}")

if bmi >= 25:
    print("You are overwieght you need to work out more and watch your diet.")

elif 18.5 <= bmi < 25:
    print("You are fit & healthy.")

elif bmi < 18.5:
    print("You are underweight. Watch your health.")