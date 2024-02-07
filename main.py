MovieNmae :str = "Avengers Endgame"
Rating : int = 3 # of 5 
popularityScore :float=72.65


if Rating >= 4 and popularityScore > 80 :

    print("Highly recommended")

elif Rating >= 3 and popularityScore > 70 :
    print("I recommended it . It is good ")

elif Rating <= 2 and popularityScore  > 60 :
    print(" You should check it out!")

elif Rating <= 2 and popularityScore  > 50 :
     print(" Don't watch it. It is a waste of time ")

else:
    print("Please enter correct values")
