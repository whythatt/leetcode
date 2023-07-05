nums = [2, 4, 25]
num = -1

for i in nums:
    if i != max(nums) and i != min(nums):
        num = i

print(num)
