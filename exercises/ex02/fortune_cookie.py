"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730314539"

from random import randint

fortune: int = int(randint(1,4))

print("Your fortune cookie says...")
if fortune == 1:
    print("Your luckiest day will happen after a bleak one!")
else:
    if fortune == 2:
        print("A favor from a friend will be called upon soon.")
    else:
        if fortune == 3:
            print("Your true love will be found only if your eyes are open.")
        else:
            if fortune == 4:
                print("Flowers and rainbows often come because of rain.")
print("Now, go spread positive vibes!")