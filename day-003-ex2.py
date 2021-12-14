# Leap year
year = int(input("Enter a year to check\n"))

if (year % 4 == 0):
    if (year % 100 == 0):
        if ( year % 400 == 0):
            print("The year is Leap")
        else: 
            print("The year is not Leap")
    else:
        print("The year is Leap")
else: 
    print("The year is not Leap")
