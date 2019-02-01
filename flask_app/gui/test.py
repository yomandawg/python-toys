import datetime

startmonth = datetime.datetime(2019, 1, 1)
endmonth = datetime.datetime(2019, 1, 31)
now = datetime.datetime.now()

diff = endmonth - startmonth

totalsec = diff.total_seconds()

totalmin = totalsec / 60

nowdiff = now - startmonth

nowsec = nowdiff.total_seconds()

pay = 1000000

# 나의 초급은
sec_pay = pay / totalsec
print(sec_pay)

# 나의 분급은
min_pay = sec_pay * 60
print(min_pay)

hour_pay = min_pay * 60
print(hour_pay)

day_pay = hour_pay * 24
print(day_pay)

# 오늘까지 번 초급
print(sec_pay * nowsec)