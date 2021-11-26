from datetime import *

year, month, day = map(int, input().split())
result_date = date(year, month, day) + timedelta(days=int(input()))
print(result_date.year, result_date.month, result_date.day)
