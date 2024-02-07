#Create a variable for the movie
movie_name:str = 'Intersteller'

#Create a variable of type int to hold the rating of the movie out of 5
rating:int = 3

#Create a popularity score of type float
popularity_score: float = 72.65

#Check if the movie rating is 4 or greater and the popularity is greater than 80
if rating >= 4 and popularity_score > 80:
    print('Highly recommended')
#else if the movie rating is 3 or greater and the popularity is greater than 70
elif rating >=3 and popularity_score > 70:
    print('I recommended it . It is good')
#else if the movie rating is 2 or less and the popularity is greater than 60
elif rating <= 2 and popularity_score > 60:
    print('You should check it out!')
#else  the movie rating is 2 or less and the popularity is less than 50 
else:
    print("Don't watch it. It is a waste of time")