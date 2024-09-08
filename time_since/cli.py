import time

from time_since.util import read_time, calculate_delta

def run():
    start = read_time()
    while True:
        delta = calculate_delta(start)
        print("\033[H\033[2J", end="")
        print(delta, end="")
        time.sleep(1)

if __name__ == "__main__":
    run()