import random

from Link import getlink, sus

link_char_count = 16

while 1:
    link_count = int(input("How many nitro links do you wanna generate : "))
    for x in range(0, link_count):
        for x in range(link_char_count):
            link_char = random.choice(sus)
        link = (''.join(random.choice(sus) for i in range(16)))
        print(getlink + link)
