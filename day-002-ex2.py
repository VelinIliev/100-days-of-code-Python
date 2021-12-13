final_year = 90

age = int(input("What is your age? "))

days = 365
weeks = 52
months = 12

years_left = final_year - age
days_left = years_left * days
weeks_left = years_left * weeks
months_left = years_left * months

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')