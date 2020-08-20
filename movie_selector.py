import sys
from pip._vendor.distlib.compat import raw_input
import xlrd
import random
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re
import xlsxwriter

class Movie:
    title = str
    rating = float
    year = int
    director = str
    actors = str
    country = str
    genre = str
    movie_list = []

    def __init__(self, title, rating, genre, length, summary, director, actors):
        self.title = title
        self.rating = rating
        self.genre = genre
        self.length = length
        self.summary = summary
        self.director = director
        self.actors = actors

    def add_movie(self, movie):
        Movie.movie_list.append(movie)

    def get_title(self, movie):
        return movie.title

    def get_rating(self, movie):
        return movie.rating

    def get_genre(self, movie):
        return movie.genre

    def get_length(self, movie):
        return movie.length

    def get_summary(self, movie):
        return movie.summary

    def get_director(self, movie):
        return movie.director

    def get_actors(self, movie):
        return movie.actors


loc = ("/Users/brandonpapin/Desktop/PycharmProjects/movie_selector/IMDB_data_new2.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
for i in range(1, sheet.nrows):
    movie = sheet.row_values(i)
    title = movie[0]
    rating = movie[1]
    genre = movie[2]
    length = movie[3]
    summary = movie[4]
    director = movie[5]
    actors = movie[6]

    movie_obj = Movie(title, rating, genre, length, summary, director, actors)
    movie_obj.add_movie(movie_obj)

seedValue = random.randrange(sys.maxsize)
random.seed(seedValue)
random_num = random.randint(0, len(Movie.movie_list))
print("\n")
print("\n")
print("Randomly selected movie is: " + Movie.get_title(movie_obj, Movie.movie_list[random_num]))
print("\n")
print("\n")
print("Rating: " + Movie.get_rating(movie_obj, Movie.movie_list[random_num]))
print("\n")
print("Genre: " + Movie.get_genre(movie_obj, Movie.movie_list[random_num]))
print("\n")
print("Length: " + Movie.get_length(movie_obj, Movie.movie_list[random_num]))
print("\n")
print("Summary: " + Movie.get_summary(movie_obj, Movie.movie_list[random_num]))
print("\n")
print("Director: " + Movie.get_director(movie_obj, Movie.movie_list[random_num]))
print("\n")
print("Lead Actors: " + Movie.get_actors(movie_obj, Movie.movie_list[random_num]))
print("\n")
print("\n")


#-----------------------------------------------
#   SCRAPING DATA AND SETTING UP DATABASE
#-----------------------------------------------

# Create a workbook and add a worksheet.
# workbook = xlsxwriter.Workbook('IMDB_data_new2.xls')
# sheet1 = workbook.add_worksheet()

# Writing to an excel
# sheet using Python

# sheet1.write(0,0, 'Title')
# sheet1.write(0,1, 'Rating')
# sheet1.write(0,2, 'Genre')
# sheet1.write(0,3, 'Length')
# sheet1.write(0,4, 'Summary')
# sheet1.write(0,5, 'Directors')
# sheet1.write(0,6, 'Actors')
# sheet1.write(1,0, 'Great Gatsby')

#   GET BASE URL AND SOURCE OF MOVIES FOR SCRAPING
# url = "https://www.imdb.com"
# top_url = "/chart/top/"
#
# try:
#     IMDB_r = requests.get(url + top_url, timeout=2)
# except requests.exceptions.RequestException:
#     raise Exception('Failed to connect to %s' % IMDB_r)
#
# IMDB_soup = BeautifulSoup(IMDB_r.text, 'html.parser')
#

# INITIALIZE COUNTERS FOR LOOPS
# i_counter = 1
# j_counter = 0

# GET HREF FROM TITLE
# links = IMDB_soup.findAll('td', {'class': 'titleColumn'})
# for link in links:
#     for href in link.findAll('a', href=True):
#             end_url = href['href']
#             new_url = url + end_url
#             IMDB_new_r = requests.get(new_url, 'html.parser')
#             IMDB_soup_spec = BeautifulSoup(IMDB_new_r.text, 'html.parser')
#
#             #  GET TITLE FROM IMDB
#             titles = IMDB_soup_spec.findAll('div', {'class': 'titleBar'})
#             for title in titles:
#                 for title_name in title.findAll('h1', {'class': ''}):
#                     movie_title = title_name.text  # load scraped data into class variable
#                     print(type(title_name.text))
#                     print(movie_title)
#                     print(type(movie_title))
#
#             #  GET RATING FROM IMDB
#             ratings = IMDB_soup_spec.findAll('div', {'class': 'title_bar_wrapper'})
#             for rating in ratings:
#                 for rating_value in rating.findAll('span', {'itemprop': 'ratingValue'}):
#                     movie_rating = rating_value.text  # load scraped data into class variable
#                     print(movie_rating)
#                     print(type(movie_rating))
#
#             #  GET GENRE FROM IMDB
#             genres = IMDB_soup_spec.findAll('div', {'class': 'subtext'})
#             genre_list = ""
#             count = 0
#             for genre in genres:
#                 for genre_name in genre.select("a[href*=genre]"):
#                     if count == 0:
#                         genre_list = genre_name.text
#                     else:
#                         genre_list = genre_list + ", " + genre_name.text
#                     count += 1
#                 movie_genre = genre_list  # load scraped data into class variable
#                 print(movie_genre)
#                 print(type(movie_genre))
#
#             #  GET LENGTH FROM IMDB
#             lengths = IMDB_soup_spec.findAll('div', {'class': 'subtext'})
#             for length in lengths:
#                 for length_value in length.findAll('time'):
#                     movie_length = length_value.text.replace(' ', '')  # load scraped data into class variable
#
#             #  GET DESC FROM IMDB
#             descriptions = IMDB_soup_spec.findAll('div', {'class': 'summary_text'})
#             for description in descriptions:
#                 movie_desc = (description.text.replace('\t', ''))  # load scraped data into class variable
#                 print(description.text)
#                 print(type(movie_desc))
#
#             #  GET DIRECTOR FROM IMDB
#             directors = IMDB_soup_spec.findAll('div', {'class': 'credit_summary_item'})[0]
#             for director_name in directors('a'):
#                 movie_director = director_name.text  # load scraped data into class variable
#                 print(director_name.text)
#                 print(type(movie_director))
#
#             #  GET ACTORS FROM IMDB
#             actors = IMDB_soup_spec.findAll('div', {'class': 'credit_summary_item'})[2]
#             actor_list = ""
#             count = 0
#             for actor_name in actors('a'):
#                 if actor_name.text != "See full cast & crew":
#                     if count == 0:
#                         actor_list = actor_name.text
#                     else:
#                         actor_list = actor_list + ", " + actor_name.text
#                     count += 1
#             movie_actors = actor_list  # load scraped data into class variable
#             print(actor_list)
#             print(type(actor_list))
#             print("adding to excel sheet")
#             print('\n')
#             sheet1.write(i_counter, j_counter, movie_title)
#             j_counter += 1
#             sheet1.write(i_counter, j_counter, movie_rating)
#             j_counter += 1
#             sheet1.write(i_counter, j_counter, movie_genre)
#             j_counter += 1
#             sheet1.write(i_counter, j_counter, movie_length)
#             j_counter += 1
#             sheet1.write(i_counter, j_counter, movie_desc)
#             j_counter += 1
#             sheet1.write(i_counter, j_counter, movie_director)
#             j_counter += 1
#             sheet1.write(i_counter, j_counter, movie_actors)
#             print(i_counter, j_counter)
#             j_counter = 0
#             print("added to excel sheet :)")
#             print('\n')
#             print('\n')
#             i_counter += 1
#
#
# workbook.close()