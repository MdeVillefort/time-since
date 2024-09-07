import time

from time_since.util import read_time, calculate_delta

def run():
    start = read_time()

    while True:
        delta = calculate_delta(start)
        print("\033[H\033[2J", end="")
        print(f"Days: {delta.days}; Hours: {delta.hours}; Minutes: {delta.minutes}; Seconds: {delta.seconds}\r", end="")
        time.sleep(1)
