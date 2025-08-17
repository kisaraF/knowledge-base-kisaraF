from datetime import time, date


# -------------- Date Object
# birthday = date(2001,12,1)
birthday = date(year = 2001, day = 1, month = 12)
# print(birthday)
# print(birthday.year)
# print(birthday.month)
# print(birthday.day)

today = date.today()
# print(today)
# print(today - birthday)


# -------------- Time Object

start = time()
# print(start)
# print(start.hour)
# print(start.minute)
# print(start.second)

new_start = time(hour=14, minute=30)
# print(new_start)


# -------------- datetime Object
from datetime import datetime as dt

new_dt = dt(year = 2001, month = 12, day = 1, hour = 19, minute = 00, second = 47)
print(new_dt)
print(dt(2001,12,1))
print(dt(2001,12,1,19))

print(dt.now())
print(dt.now()-new_dt)