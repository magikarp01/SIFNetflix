import numpy as np
import pandas as pd
import pickle
import math

dataframe1 = pd.read_excel("Netflix Dataset Latest 2021.xlsx")
# print(dataframe1)
tags = dataframe1["Tags"]
imdb_reviews = dataframe1["IMDb Score"]
summaries = dataframe1["Summary"]
print(imdb_reviews)

# getting the genres
genre_column = dataframe1["Genre"]
imdb_column = dataframe1["IMDb Score"]

# list of possible genres

movie_genres = []
genres = []
imdb_reviews = []
for i in range(len(genre_column)):
    genre_cell = genre_column[i]
    if genre_cell is not None and imdb_column[i] is not None and not math.isnan(imdb_column[i]):
        try:
            cell_genres = genre_cell.split(", ")
            movie_genres.append(cell_genres)
            imdb_reviews.append(imdb_column[i])
        except AttributeError:
            continue
        for genre in cell_genres:
            if genre not in genres:
                genres.append(genre)

genres_file_name = 'movie_genres.pk'
with open(genres_file_name, 'wb') as fi:
    pickle.dump(movie_genres, fi)

reviews_file_name = 'reviews.pk'
with open(reviews_file_name, 'wb') as fi:
    pickle.dump(imdb_reviews, fi)


# print(genres)
# print(len(genres))