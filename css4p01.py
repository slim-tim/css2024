# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:07:21 2024

@author: dell user
"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")
# print(df)
# df.head()
# print(df.info())

# 1. What is the highest rated movie in the dataset?
df['Rating']
df['Rating'].idxmax()
highest_rated_movie = df.loc[df['Rating'].idxmax()]['Title']
print('The highest rated movie is:', highest_rated_movie)

# 2. What is the average revenue of all movies in the dataset? 
df1 = df['Revenue (Millions)'].dropna()
average_revenue1 = df1.mean()
print('Average revenue of all movies dropping missing values:', average_revenue1, 'million')

median_value = df['Revenue (Millions)'].median()
df2 = df['Revenue (Millions)'].fillna(median_value)
average_revenue2 = df2.mean()
print('Average revenue of all movies after filling missing values:', average_revenue2, 'million')

# 3. What is the average revenue of movies from 2015 to 2017 in the dataset?
movies_15_17 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_15_17a = movies_15_17['Revenue (Millions)'].mean()
print('Average revenue of movies between 2015 and 2017 without filling missing values:', average_revenue_15_17a, 'million')

median_value2 = movies_15_17['Revenue (Millions)'].median()
movies_15_17b = movies_15_17['Revenue (Millions)'].fillna(median_value2)
average_revenue_15_17b = movies_15_17b.mean()
print('Average revenue of movies between 2015 and 2017 after filling missing values:', average_revenue_15_17b, 'million')

# 4. How many movies were released in the year 2016?
movies_2016 = df[(df['Year'] == 2016)].shape[0]
print('Number of movies released in 2016:', movies_2016)

# 5. How many movies were directed by Christopher Nolan?
nolan_movies = df[(df['Director'] == 'Christopher Nolan')].shape[0]
print('Number of movies movies directed by Christopher Nolan:', nolan_movies)

# 6. How many movies in the dataset have a rating of at least 8.0?
ratings_8 = df[(df['Rating'] >= 8)].shape[0]
print('Number of movies with a rating of at least 8.0:', ratings_8)

# 7. What is the median rating of movies directed by Christopher Nolan?
nolan_rating = df[(df['Director'] == 'Christopher Nolan')]['Rating'].median()
print('The median rating of movies directed by Christopher Nolan:', nolan_rating)

# 8. Find the year with the highest average rating?
average_rating_by_year = df.groupby('Year')['Rating'].mean()
print('The year with the highest average rating:', average_rating_by_year.idxmax())

# 9. What is the percentage increase in number of movies made between 2006 and 2016?
movies_2006_count = df[df['Year'] == 2006].shape[0]
movies_2016_count = df[df['Year'] == 2016].shape[0]
percentage_increase = ((movies_2016_count - movies_2006_count) / movies_2006_count) * 100
print('Percentage increase in number of movies between 2006 and 2016:', percentage_increase,'%')

# 10. Find the most common actor in all the movies?
all_actors = ', '.join(df['Actors'].dropna())
all_actor_list = [actor.strip() for actor in all_actors.split(',')]
actor_counts = pd.Series(all_actor_list).value_counts()
most_common_actor = actor_counts.idxmax()
print('Most common actor in all moovies:', most_common_actor)

# 11. How many unique genres are there in the dataset?
all_genres = ', '.join(df['Genre'].dropna())
all_genre_list = [genre.strip() for genre in all_genres.split(',')]
unique_genres = set(all_genre_list)
num_unique_genres = len(unique_genres)
print("Number of unique genres:", num_unique_genres)

# 12. Do a correlation of the numerical features, what insights can you deduce? 
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numerical_columns].corr()
print('Correlation Matrix:', correlation_matrix)


