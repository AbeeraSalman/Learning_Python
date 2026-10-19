marks=85
if marks>85:
    print("A Grade")
elif marks<85:
    print("B- Grade")
else:
    print("B- Grade")


#loops
#Lists
names=["Abeera","Hooria","Moona"]
for name in names:
    print(name)
names.append("Aisha")
print(len(names))
#Tuples
coordinates=(10,20)
x,y=coordinates
print(x,y)
#coordinates[0]=5  "TypeError: 'tuple' object does not support item assignment"

#Sets
nums={1,2,3,4,2,4}
print(nums)
print(6 in nums)
print({1,2}| {3,2})
print({1,2} & {2,3})













