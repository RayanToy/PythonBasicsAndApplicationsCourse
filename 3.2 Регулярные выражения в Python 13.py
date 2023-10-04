import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\ba+\b', 'argh', line, count=1, flags=re.IGNORECASE))