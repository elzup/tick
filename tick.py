import time
from datetime import datetime

min1 = 60

while True:
  tdatetime = datetime.now()
  print(tdatetime.strftime('%Y-%m-%dT%H:%M:%S'))
  time.sleep(min1)
