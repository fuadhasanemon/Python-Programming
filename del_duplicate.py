# One way out of many ways. Xotil way.
a = [1,1,2,3,4,5,2,1,1,3]

b = a.copy()

# This takes account of how many items are deleted.
x = 0

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            del b[i-x]
            x = x+ 1
            break

print(b)
print(a)