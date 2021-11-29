import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\b[Aa]+\b", "argh", line, count=1))
