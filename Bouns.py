# - Ask the user to provide his wieght.
wieght:float =float(input("Enter your wieght in kg")) 
# - Ask the user to provide hi height.
height:int =int(input("Enter your height in cm"))

# - print the BMI for the user.
# - using conditionals tell the user that either :
# - - You are overwieght you need to work out more and watch your diet.
# - - You are fit & healthy.
# - - You are underweight. Watch your health.

BMI =(wieght/(height/100)**2)

if BMI<=18.5:
    print("You are underweight. Watch your health.")
elif BMI>=18.5 and BMI<=24.9:
    print("You are fit & healthy")
else: 
    print("You are overwieght you need to work out more and watch your diet")
    
