
Wieght = int(input("Enter your wieght (in KG)"))
Height = int(input("Enter your height (in cm)"))

IBM = Wieght / (Height/100)**2
x = "Your IBM : {:.2f}".format(IBM)
print(x)


if IBM >= 25 :
    print("You are overwieght you need to work out more and watch your diet")

elif IBM >= 18.5 :
    print("You are fit & healthy")

elif IBM <=18 :
    print("You are underweight. Watch your health")

else :
    print("Please enter correct values")
