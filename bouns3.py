#Ask the user to provide his wieght.
wieght:float = float(input("Enter your wieght")) 

#Ask the user to provide hi height.
height:float = float(input("Enter your height"))
height = height/100
 #print the BMI for the user.
BMI:float = wieght/height**2
print(BMI)
#using conditionals tell the user that either :
if BMI >= 30:
    print("You are overwieght you need to work out more and watch your diet.")

if BMI >=18.5:
    print("You are fit & healthy.")
    
if BMI <= 18.5:
   print(" You are underweight. Watch your health.") 