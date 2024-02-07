wieght:int= input("Your Wieght:  ")
Height:int= input("Your Height:  ")
BMI= wieght/Height**2
if BMI >50: 
    print("You are overwieht need to work out more and watch your diet")
elif BMI <=45 :
    print("You are fit& healthy")
elif BMI <40 :
    print("You are underweght. Watch your health")
