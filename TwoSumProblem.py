#Two Sum problems

nums = [1, 2, 3, 4, 5, 6]

print("Numbers in the list:", nums)
target = int(input("Enter a target number (the sum of two numbers from the list): "))

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print(f"{nums[i]} and {nums[j]} and (indexes are {i} and {j}")



