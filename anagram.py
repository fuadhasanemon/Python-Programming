str1 = 'zingalala'
str2 = 'lalanagzi'


d1 = dict()
d2 = dict()

for i in range(0,len(str1)):
    if str1[i] not in d1:
        d1[str1[i]] = 0

    else:
        d1[str1[i]] +=1

for i in range(0,len(str2)):
    if str2[i] not in d2:
        d2[str2[i]] = 0

    else:
        d2[str2[i]] +=1

x = 0
for key in d1.keys():
    x  += 1
    if key in d2 and d1[key] == d2[key]:
        pass
    else:
        print("Not anagram")
        break
    if (x== len(d1.keys())):
        print("Anagram")