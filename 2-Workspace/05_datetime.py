from datetime import date

today = date.today()
print(today)

print(today.day)
print(today.month)
print(today.year)

print(today.weekday())
print(today.isoweekday())

past_date = date(2015, 8, 13)
print(past_date)


from datetime import datetime

now = datetime.now()
print(now)
print(now.ctime())
print(datetime.ctime(now))
print(now.date())
print(now.time())
