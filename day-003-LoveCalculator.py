print("Welcome to love calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

# .lower()
# count()
two_names = name1.lower() + name2.lower()
# print(two_names)

t = two_names.count('t')
r = two_names.count('r')
u = two_names.count('u')
e = two_names.count('e')

true_score = str(t+r+u+e)

l = two_names.count('l')
o = two_names.count('o')
v = two_names.count('v')
e = two_names.count('e')

love_score = str(l+o+v+e)

truelove_score = int(true_score + love_score)

# print(truelove_score)

if (truelove_score < 10) or (truelove_score > 90):
    print(f"Your score is {truelove_score}, you go together like coke and mentos.")
elif (truelove_score >= 40) or (truelove_score <= 50):
    print(f"Your score is {truelove_score}, you are alright together.")
else: 
    print(f"Your score is {truelove_score}.")

