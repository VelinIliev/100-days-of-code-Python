from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_itallic(function):
    def wrapper():
        return f"<i>{function()}</i>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
@make_bold
@make_itallic
@make_underline
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/bye")
def say_bye():
    return "<h1 style='text-align:center'>Bye</h1>" \
            "<p>This is paragraph</p>" \
            "<div class='test'>This is div</div>"
    

# @app.route("/<name>/1")
# def greet(name):
#     return f'<h1>Hello {name.capitalize()}!</h1>'

# @app.route("/<path:name>")
# def greet(name):
#     return f'<h1>Hello {name.capitalize()}!</h1>'

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f'<h1>Hello {name.capitalize()}, you are {number} years old!</h1>'

if __name__ == "__main__":
    app.run(debug=True)