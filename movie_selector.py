import sys

import xlrd
import random
from datetime import datetime

from pip._vendor.distlib.compat import raw_input


class Movie:
    title = str
    rating = float
    year = int
    director = str
    actors = str
    country = str
    genre = str
    movie_list = []

    def __init__(self, title, director, actors, year, rating, country, genre):
        self.title = title
        self.rating = rating
        self.year = year
        self.director = director
        self.actors = actors
        self.country = country
        self.genre = genre

    def add_movie(self, movie):
        Movie.movie_list.append(movie)

    def get_title(self, movie):
        return movie.title

    # returns genre of movie
    def get_genre(self, movie):
        return movie.genre

    def get_director(self, movie):
        return movie.director

    def get_actors(self, movie):
        return movie.actors

    def get_country(self, movie):
        return movie.country

    def get_rating(self, movie):
        return movie.rating

    def get_year(self, movie):
        return movie.year


loc = ("/Users/brandonpapin/Downloads/Copy of Greatest films of all time(1).xlsx")
wb = xlrd.open_workbook(loc)
sheetNames = wb.sheet_names()
sheet_list = []
for i in sheetNames:
    sheet_list.append(tuple((wb.sheet_by_name(i), i)))

for i in range(len(sheet_list)):
    sheet = wb.sheet_by_index(i)

    for j in range(1, sheet.nrows):
        movie = sheet.row_values(j)
        title = movie[0]
        director = movie[1]
        actors = movie[2]
        year = movie[3]
        rating = movie[4]
        country = movie[5]
        genre = str(sheet_list[i])

        movie_obj = Movie(title, director, actors, year, rating, country, genre)
        movie_obj.add_movie(movie_obj)

# for i in range(len(Movie.movie_list)):
#     print(Movie.get_genre(movie_obj, Movie.movie_list[i]))
#     print("\n")


seedValue = random.randrange(sys.maxsize)
random.seed(seedValue)
random_num = random.randint(0, len(Movie.movie_list))
print("\n")
print("\n")
print("Randomly selected movie is: " + Movie.get_title(movie_obj, Movie.movie_list[random_num]))
print("\n")
print("\n")
print("Show additional info? Y/N")
choice = raw_input()
print("\n")

if (choice == 'Y'):
    print("Genre: " + Movie.get_genre(movie_obj, Movie.movie_list[random_num]))
    print("\n")
    print("Director: " + Movie.get_director(movie_obj, Movie.movie_list[random_num]))
    print("\n")
    print("Lead Actors: " + Movie.get_actors(movie_obj, Movie.movie_list[random_num]))
    print("\n")
    print("Year Released: " + str(Movie.get_year(movie_obj, Movie.movie_list[random_num])))
    print("\n")
    print("Rating: " + str(Movie.get_rating(movie_obj, Movie.movie_list[random_num])))
    print("\n")
    print("Country: " + str(Movie.get_country(movie_obj, Movie.movie_list[random_num])))
    print("\n")
    print("\n")