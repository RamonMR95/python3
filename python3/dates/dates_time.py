import time
import datetime


epoch_seconds = time.time()
print(epoch_seconds)

t = time.ctime(epoch_seconds)
print(t)

dt = datetime.datetime.today()
print(dt)
print(dt.day, dt.month, dt.year, sep="/")
print("Current date: {}/{}/{}".format(dt.day, dt.month, dt.year))


# Getting today's date
today = datetime.date.today()
print(today)

another_date = datetime.datetime(2015, 3, 15)
print(another_date)
print(another_date.strftime('%A'))  # WeekDay
print(another_date.strftime('%w'))  # WeekDay as a number
print(another_date.strftime('%B'))  # Month
print(another_date.strftime('%m'))  # Month as a number
print(another_date.strftime('%Y'))  # Year
print(another_date.strftime('%C'))  # Day of Month
print(another_date.strftime('%D'))  # Month, Day, Year
print(another_date.strftime('%H'))  # Hour

