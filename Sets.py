
nums = {1, 2, 3, 3, 2}
print(nums)
empty = set()  #empty dict
 #nums[0]  #no indexing


class_a = {"Moona", "Aisha", "Sara"}
class_b = {"Aisha", "Hira", "Sara"}
print(class_a & class_b)
print(class_a | class_b)
print(class_a.difference((class_b)))
print(class_b.difference((class_a)))





# Frozenset
f = frozenset({"Aisha", "Sara"})
print(f)
#we can add or remove to frozenset by using these operators
new_f = f | {"Noor"}   # add
new_f = new_f - {"Aisha"}   # remove
print(new_f)
