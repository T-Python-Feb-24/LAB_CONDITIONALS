weight =float(input("user to provide his weight"))
height =float(input("user to provide his height"))
x = weight / (height/100)**2
print(x)
if x < 18.5:
    print('You are overwieght you need to work out more and watch your diet')
elif x  <25:
    print("You are fit & healthy")
elif x <= 18 :
   print('You are underweight. Watch your health')
else:
   print("rong value")