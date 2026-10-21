#first non-repeating character
from itertools import count

name=input("Enter a string:")
name=name.lower()
counts= {}
for i in name:
    count=0
    for j in name:
        if i!=j:
            continue
        else:
            count+=1
            counts[i]=count

for i in counts:
    if counts[i]==1:
        print(i)
        break




#Most frequent element in a string

name=input("Enter a string:")
name=name.lower()
counts= {}
for i in name:
    count=0
    for j in name:
        if i!=j:
            continue
        else:
            count+=1
            counts[i]=count

max_count=0
for i in counts:
    if counts[i]>max_count:
        max_count=counts[i]
for j in counts:
    if counts[j]==max_count:
        print(j)

sec_largest=0
for k in counts:
    if counts[k]< max_count and counts[k]>sec_largest:
        sec_largest=counts[k]




