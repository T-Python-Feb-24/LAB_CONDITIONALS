movie:str = input("Enter the movie name: ")
rating:float = float(input("Enter the movie rating out of 5: "))
popularity:float = float(input("Enter the movie popularity out 0f 100: "))

if rating >= 4 and popularity > 80:
    print("Highly recommended")

elif rating >=3 and popularity > 70:
    print("I recommended it . It is good")

elif rating <= 2 and popularity > 60:
    print("You should check it out!")

else: 
    print("Don't watch it. It is a waste of time")