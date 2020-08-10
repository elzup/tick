import time
from datetime import datetime

while True:
  print(datetime.now().isoformat()[:-7])
  time.sleep(1)
