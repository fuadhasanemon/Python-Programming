import random

a = [x for x in range(0,101)]

random.shuffle(a)

# Random value removing
del a[32]
del a[33]
del a[55]
del a[31]

a.sort()

for i in range(0,len(a)):
    if i not in a:
        print(i)

