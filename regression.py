import numpy as np
import pandas as pd
import pickle
with open('movie_genres.pk', 'rb') as fi:
    movie_genres = pickle.load(fi)

with open('reviews.pk', 'rb') as fi:
    imdb_reviews = pickle.load(fi)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing

genres = ['Crime', 'Drama', 'Fantasy', 'Horror', 'Romance', 'Comedy', 'Mystery', 'Thriller', 'Short', 'Action', 'Adventure', 'Sci-Fi', 'Music', 'Animation', 'Family', 'Biography', 'War', 'History', 'Documentary', 'Film-Noir', 'Sport', 'Game-Show', 'Western', 'Musical', 'Reality-TV', 'News', 'Talk-Show', 'Adult']

genredict = {k: v for v, k in enumerate(genres)}
x_data = []
for movie in movie_genres:
    movie_data = [0]*len(genres)
    for genre in movie:
        movie_data[genredict[genre]] = 1
    x_data.append(movie_data)

print(x_data)