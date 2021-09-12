"""An example, simple program"""

i: int = 0
s: str = ""

while i < 10:
    if i % 2 == 0:
        s = s + "h"
    else:
        s = s + "e"
    i = i + 1

print(s)