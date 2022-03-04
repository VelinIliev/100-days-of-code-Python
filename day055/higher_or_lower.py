from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(1, 10)
print(random_number)

@app.route("/")
def start():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route("/<int:number>")
def chek_number(number):
    if number > 10 or number < 1:
        return "<h1 style='color:red'>The number is between 1 and 10</h1>"
    elif number > random_number:
        return "<h1 style='color:black'>Your number is too high</h1>"
    elif number < random_number:
        return "<h1 style='color:blue'>Your number is too low</h1>"
    elif number == random_number:
        return "<h1 style='color:orange'>Your guess the number</h1>"

@app.route("/<string>")
def error(string):
    return "<h1 style='color:red'>Please enter a number</h1>"

if __name__ == "__main__":
    app.run(debug=True)