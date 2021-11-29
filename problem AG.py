import sys
import re


def is_divide_on_three(number):
    if int(number, 2) % 3 == 0:
        return True
    else:
        return False


for line in sys.stdin:
    line = line.rstrip()
    if re.match(r"\b([01][01]+)|(^[01]$)", line):
        if is_divide_on_three(line):
            print(line)
