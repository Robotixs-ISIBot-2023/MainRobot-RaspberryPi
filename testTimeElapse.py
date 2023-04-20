import time

start = time.time()
print(start)

time.sleep(10)  # or do something more productive

done = time.time()
elapsed = done - start
print(elapsed)
