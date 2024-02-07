wieght_num:float= float(input("your wieght: "))
hieght_num:float= float(input("your hieght: "))
calculate_bmi =wieght_num / ((hieght_num/100)**2)
print(float(calculate_bmi))
if calculate_bmi>=39:
   print("u are overwieght you need to work out more and watch your diet")
elif calculate_bmi>=25:
   print("u are fit & healthy")
else:
   print(" You are underwieght.watch your health") 

