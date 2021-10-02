import requests
from bs4 import BeautifulSoup

response = requests.get(url="http://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text
# print(website_html)


soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())
all_movie = (soup.find_all(name="h3", class_="title"))
print(all_movie)
movie_titles = [movie.getText() for movie in all_movie]
movie_titles.reverse()
print(movie_titles)

with open("movies.txt", mode="w") as file:
    for movie in movie_titles:
        data = file.write(f"{movie}\n")


