import random
import time

x = []
min = int(input("Please press Minimum value:"))
max = int(input("Please press Maximum value:"))
while (len(x) < max - 1):
    time.sleep(1)
    num = random.randrange(min, max)
    if (num in x):
        num = random.randrange(min, max)
    else:
        x.append(num)
        print(num)
        value = input("Please press Enter for the next number:")
