from flask import Flask
from flask import render_template
import random
import datetime
import requests

blog_posts = [
    {
    "id": 1,
    "title": "The Life of Cactus",
    "subtitle": "Who knew that cacti lived such interesting lives.",
    "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify."
  },
  {
    "id": 2,
    "title": "Top 15 Things to do When You are Bored",
    "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
    "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today."
  },
  {
    "id": 3,
    "title": "Introduction to Intermittent Fasting",
    "subtitle": "Learn about the newest health craze.",
    "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake."
  }
]

app = Flask(__name__)

def get_gender(name):
    URL = f"https://api.genderize.io/?name={name}&country_id=BG"
    response = requests.get(URL)
    content = response.json()
    return content["gender"]

def get_age(name):
    URL = f"https://api.agify.io/?name={name}&country_id=BG"
    response = requests.get(URL)
    content = response.json()
    return content["age"]

def get_blog():
    URL = f"https://www.npoint.io/docs/c790b4d5cab58020d391"
    response = requests.get(URL)
    content = response.json()
    return content

@app.route("/")
def index():
    random_number = random.randint(1,10)
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    current_date = f'{current_day:02}-{current_month:02}-{current_year}'
    return render_template("index.html", num = random_number, date = current_date)

@app.route("/guess/<name>")
def guess(name):
    gender = get_gender(name)
    age = get_age(name) 
    return render_template("guess.html", name = name, gender = gender, age = age)

# @app.route("/blog/")
# def blog2():
#     return render_template("blog.html", posts = blog_posts)

@app.route("/blog/<num>")
def blog(num):
    num = int(num)
    print(type(num))
    return render_template("blog.html", posts = blog_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)