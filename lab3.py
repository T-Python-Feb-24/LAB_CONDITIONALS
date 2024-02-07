movie_name:str="the walking dead"
rating_movie:int= 3
popularity_score:float=72.65
if rating_movie >=4 and popularity_score >80:
    print("highly recommended")
elif rating_movie >= 3 and popularity_score >70:
    print("I recommended it , it is good")
elif rating_movie <= 2 and popularity_score >60:
    print("you should check it out!")
elif rating_movie <= 2 and popularity_score <50:
    print("Don't watch it , it is a waste of time ")



