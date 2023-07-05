nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
num = 0
for i in range(len(nums) + 1):
    if not i in nums:
        num = i

print(num)
