from bs4 import BeautifulSoup
import requests

# with open("./website.html", mode = "r") as file:
#     content = file.read()


# soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# all_li = soup.find_all(name="li")
# all_a = soup.find_all(name="a")

# for li in all_li:
#     print(li.getText())

# for a in all_a:
#     print(a.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# print(soup.select(".heading"))

response = requests.get("https://news.ycombinator.com/")
content = response.text

soup = BeautifulSoup(content, "html.parser")

titles = soup.find_all(name="a", class_="titlelink")
title_texts = []
title_links = []

for title in titles:
    text = title.text
    title_texts.append(text)
    link = title.get("href")
    title_links.append(link)

titles_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

# print(title_texts[0])
# print(title_links[0])
max_score = max(titles_upvotes)
max_index = titles_upvotes.index(max_score)

print(title_texts[max_index])
print(title_links[max_index])
print(f'score: {max_score}')