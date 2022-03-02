import time 

def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
        print("*"*30)
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello")
    
@decorator_function
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_hello()
say_bye()
decorated_function = decorator_function(say_greeting)
decorated_function()