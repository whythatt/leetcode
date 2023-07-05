nums = [1, 3, 5, 6]
target = int(input("Enter number: "))


def search_position():
    count = 0
    for i in nums:
        if target <= i:
            continue
        elif target >= i:
            count += 1
    return count


if target in nums:
    print(nums.index(target))
else:
    print(search_position())
