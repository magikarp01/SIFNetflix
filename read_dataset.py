import numpy as np
import pandas as pd

dataframe1 = pd.read_excel("Netflix Dataset Latest 2021.xlsx")
# print(dataframe1)
tags = dataframe1["Tags"]
imdb_reviews = dataframe1["IMDb Score"]
summaries = dataframe1["Summary"]
print(imdb_reviews)