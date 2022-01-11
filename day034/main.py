# declaring data type of variable
age: int
name: str
height = float
is_human: bool

# declaring data type of function input and output
def police_check(age: int) -> bool:
    if age >= 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(12):
    print("Can drive")
else: 
    print("Going to jail")