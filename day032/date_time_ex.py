import datetime as dt

def now2():
    now1 = dt.datetime.now()
    return now1

print(now2())
print(now2())

now = dt.datetime.now()
print(now.year)

print(now.month)
print(now.day)
weekdays = ["Понеделник", "Вторник", "Сряда", "Четвъртък", "Петък", "Събота", "Неделя"]
# if now.weekday() == 0:
#     weekday = "Понеделник"
# elif now.weekday() == 1:
#     weekday = "Вторник"
# elif now.weekday() == 2:
#     weekday = "Сряда"
# elif now.weekday() == 3:
#     weekday = "Четвъртък"
# elif now.weekday() == 4:
#     weekday = "Петък"
# elif now.weekday() == 5:
#     weekday = "събота"
# elif now.weekday() == 6:
#     weekday = "Неделя"
weekday = weekdays[now.weekday()]
print(f'weekday: {weekday}')

print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

velin_date_of_birth = dt.datetime(year=1977, month=4, day=29, hour=22)
print(velin_date_of_birth.year, velin_date_of_birth.month, velin_date_of_birth.day, velin_date_of_birth.hour)
print(velin_date_of_birth)