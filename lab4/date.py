import datetime

#1
current_date = datetime.datetime.now()
delta = datetime.timedelta(days = 5)
new_date = current_date - delta
print(new_date)

#2
current_date = datetime.datetime.now()
delta = datetime.timedelta(days = 1)
today = current_date
tomorrow = current_date + delta
yesterday = current_date - delta
print(today)
print(tomorrow)
print(yesterday)

#3
current_date = datetime.datetime.now()
print(current_date.strftime('%Y-%m-%d %H:%M:%S'))

#4
current_date = datetime.datetime.now()
delta = datetime.timedelta(days = 1)
today = current_date
tomorrow = current_date + delta
date_difference = tomorrow - today
difference_in_seconds = date_difference.total_seconds()
print(difference_in_seconds)

