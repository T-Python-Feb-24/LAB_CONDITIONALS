#Movie info
movie:str = "Enola"
movie_rating:int = 3
popularity_score:float = 72.65

#Ckeck recommendations
if movie_rating >= 4 and popularity_score > 80:
    print("Highly recommended")
elif movie_rating >= 3 and popularity_score > 70:
    print("I recommended it . It is good")
else: 
    print("Don't watch it. It is a waste of time") 


