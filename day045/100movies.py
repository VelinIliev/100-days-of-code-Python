from bs4 import BeautifulSoup
import requests

# https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content, "html.parser")

titles = soup.find_all(name="h3", class_="title")
temp = [title.text for title in titles]
top100movies = temp[::-1]

for title in top100movies:
    print(title)

with open("movies.txt", mode="w") as file:
    for movie in top100movies:
        file.write(f'{movie}\n')