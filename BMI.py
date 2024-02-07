try:
    user_wieght = float(input("Enter your wieght in (Kg):"))
    user_height = float(input("Enter your height in(meter):"))
except ValueError:
    print("Wrong entry only numbers allowed")
    exit(1)

# BMI calculation
bmi = user_wieght/(user_height**2)
print(f"BMI calculation: {bmi}")
# conditional expressions
if bmi >= 25:
    print("You are overwieght you need to work out more and watch your diet")
elif bmi >= 18.5 and bmi < 25:
    print("You are fit & healthy")
else:
    print("You are underweight. Watch your health")
