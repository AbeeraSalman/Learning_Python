from array import array

nums=[ "i" ,1,2,3,4]
def is_even(num):
    if num%2==0:
        return True
    else:
       return False


for i in range(10):
    if is_even((i)):
        print(i)





numbers=input("Enter numbers separated by a comma")
parts=numbers.split(",")
a=int(parts[0])
b=int(parts[1])
print(f"the value of a is {a} and b is {b}")
