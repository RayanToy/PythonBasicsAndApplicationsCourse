import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\\.{1,}', line):
        print(line)

