from datetime import *
import time

# CHECK EXECUTION TIME
start = time.perf_counter()

l_dates = []

d1 = date(2016, 6, 9)
d2 = date(2017, 6, 7)
d3 = date(2019, 4, 5)

l_dates.append(d1)
l_dates.append(d2)
l_dates.append(d3)

l_dates.sort()

# SLEEP METHOD
time.sleep(3)

print(l_dates)

end = time.perf_counter()

print("Total of time: ", end - start)
