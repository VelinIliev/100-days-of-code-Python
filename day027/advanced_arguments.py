def my_function(a=1, b=2, c=3):
    """ describe the function """
    return f'a: {a}, b: {b}, c: {c}'

print(my_function(b=4))
    
def add(*args):
    # print(args[3])
    sum = 0 
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    # print(kwargs["add"])
    if 'multiply' not in kwargs:
        kwargs['multiply'] = 1
    if 'add' not in kwargs:
        kwargs['add'] = 0
    if 'substract' not in kwargs:
        kwargs['substract'] = 0
    if 'divide' not in kwargs:
        kwargs['divide'] = 1

    n += kwargs['add']
    n *= kwargs['multiply']
    n -= kwargs['substract']
    n /= kwargs['divide']
    return n


print(calculate(2, add=3, multiply=22))

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        
my_car = Car(make = "Nissan", model="GTR")
print(my_car.make, my_car.model)