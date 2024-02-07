# - Create a variable for the movie (choose any movie you like)
moveName:str = 'Batman'
# - Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
moveRating:int = 3
# - Create a popularity score of type float , let it be 72.65
movePopularity:float =72.65

# - Using an if statement 
# - - Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if moveRating>=4 and movePopularity>80:
    print("Highly recommended")
    
# - - else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
elif moveRating>=3 and movePopularity>70:
    print("I recommended it . It is good")
    
# - - else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
elif moveRating>=2 and movePopularity>60:
    print("You should check it out!")
# -  - else  the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
else: 
    print("Don't watch it. It is a waste of time")
    

