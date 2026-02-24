#5 days from now
from datetime import datetime, timedelta
n = datetime.now() - timedelta(days=5)
print(n.strftime("%Y-%m-%d"))

#yest, tod, tmr
t = datetime.now()
print("Yesterday:", (t - timedelta(days=1)).strftime("%Y-%m-%d"))
print("Today:", t.strftime("%Y-%m-%d"))
print("Tomorrow:", (t + timedelta(days=1)).strftime("%Y-%m-%d"))

#drop microsecs
dt = datetime.now().replace(microsecond=0)
print(dt)

#days diff in secs
d1 = datetime.strptime(input("Date 1 (Y-M-D H:M:S): "), "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(input("Date 2 (Y-M-D H:M:S): "), "%Y-%m-%d %H:%M:%S")
diff = abs((d2 - d1).total_seconds())
print(int(diff))