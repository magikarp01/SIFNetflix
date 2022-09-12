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
x_data = np.array(x_data)

y_data = np.array(imdb_reviews)/10
print(y_data)

X_train, X_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.3, random_state=101)

# creating a regression model
model = LinearRegression()

# fitting the model
model.fit(X_train, y_train)

# making predictions
predictions = model.predict(X_test)

for i in range(len(y_test)):
    print(f"predicts {predictions[i]}, actual review is {y_test[i]}")

# model evaluation
print('mean_squared_error : ', mean_squared_error(y_test, predictions))
# print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print(f'model R^2: {model.score(X_test, y_test)}')
# print(f'model coefficients: {model.coef_}')

coef_dic = dict(zip(genres, model.coef_))
for k, v in coef_dic.items():
    print(f"For genre {k}, the coefficient is {v}")