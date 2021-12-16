print("Welcome to rollercaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if (height > 120):
    print("You can ride.")
    age = int(input("What is your age?\n"))
    if (age < 12):
        bill += 5
        print("Child tickets are $5")
    elif (age <= 18):
        bill += 7
        print("Youth tickests are $7")
    elif (age >= 45 and age <= 55):
        bill += 0
        print("Youth tickests are $0")
    else: 
        bill += 12
        print("Adult tickets are $12")

    photo = input("Do you want a photo? Y ot N\n")
    
    if photo == "Y":
        bill += 3
    
    print(f"Your bill is: ${bill:.2f}")

else: 
    print("You can't ride.")

