import datetime

today = datetime.date.today()
lastofprevmonth = (today.replace(day=1)) - datetime.timedelta(days=1)
firstofprevmonth = lastofprevmonth.replace(day=1)
