import time
from datetime import datetime

min1 = 60

while True:
  print(datetime.now().isoformat()[:-7])
  time.sleep(min1)
