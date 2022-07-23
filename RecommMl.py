# simple python recommendation program
import pandas as pd
import sys 
movie_check=sys.argv[1]
path=r"C:\Users\Igbinedion Uyiosa\Downloads\Compressed\file.tsv"  
rats = pd.read_csv(path, sep='\t')
rats.columns=['user_id', 'item_id', 'rating', 'timestamp']
movie_titles = pd.read_csv(r"C:\Users\Igbinedion Uyiosa\Downloads\Compressed\Movie_Id_Titles.csv")
data = pd.merge(rats, movie_titles, on='item_id')
ratings=pd.DataFrame(data.groupby('title')['rating'].mean()) 
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())
moviemat=data.pivot_table(index ='user_id', columns ='title', values ='rating')

def recomm_movie(movie):
    starwars_user_ratings = moviemat[movie] 
    similar_to_starwars= moviemat.corrwith(starwars_user_ratings)
    corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation'])
    corr_starwars.dropna(inplace = True)
    corr_starwars = corr_starwars.join(ratings['num of ratings'])
    print( corr_starwars[corr_starwars['num of ratings']>=100].sort_values('Correlation', ascending = False).head(10))

recomm_movie(movie_check)

