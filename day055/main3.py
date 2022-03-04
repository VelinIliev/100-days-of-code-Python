class User:
    def __init__(self, name):
        self.name = name
        self.islogedin = False

def isloged_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].islogedin == True:
            function(args[0])
    return wrapper


@isloged_decorator
def create_blog_post(user):
    print(f"This is {user.name} new blog post.")

new_user = User("Velko")
new_user.islogedin = True
create_blog_post(new_user)