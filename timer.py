import time
import os

previous = time.time()

texte = """
hello, world!

This is like documentation but in real time

Thank you for your attention!
Best Wishes,
Nikita
"""

while True:
    now = time.time()
    
    if (now - previous) > 1:
        os.system("cls")
        print(time.ctime()[11:-5])
        print(texte)
        previous = now