import time
import datetime

try:
    with open("datetime.txt") as f:
        start = datetime.datetime.fromisoformat(f.read().strip())
except:
    pass

while True:
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    time_elapsed = now - start
    days = time_elapsed.days
    hours, remainder = divmod(time_elapsed.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Days: {days}; Hours: {hours}; Minutes: {minutes}; Seconds: {seconds}\r", end="")
    time.sleep(1)
