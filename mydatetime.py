import datetime

tdate = datetime.datetime(2024, 1, 15)
print(tdate)

tdate = datetime.datetime.today()
print("today-date:", tdate)
print("year", tdate.year)
print("month", tdate.month)
print("day", tdate.day)
print("hour", tdate.hour)
print("minutes", tdate.minute)
print("seconds", tdate.second)

wday = tdate.weekday()
print("weekday", wday)

isowday = tdate.isoweekday()
print("ISOweekday", isowday)

tdelta = datetime.timedelta(days=5)
print("timedelta", tdate+tdelta)
print("timedelta", tdate-tdelta)

