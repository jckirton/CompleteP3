import sys
import time


def spinning_cursor():
    while True:
        for cursor in "|/-\\|":
            yield cursor


spinner = spinning_cursor()
for _ in range(10):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(.2)
    sys.stdout.write("\b")
