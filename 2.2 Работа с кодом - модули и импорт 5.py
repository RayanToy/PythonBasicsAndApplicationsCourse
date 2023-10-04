from datetime import timedelta, datetime
(y, m, d) = [int(n) for n in input().split()]
now = datetime(y, m, d)
a = now + timedelta(int(input()))
print(a.year, a.month, a.day)
