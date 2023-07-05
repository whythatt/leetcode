# 12310
# [1, 2, 3, 1, 0]
array = [9, 9]
number = ""


def split(number):
    for i in array:
        number += str(i)
    number = int(number) + 1
    return number


output = [int(x) for x in str(split(number=number))]
print(output)
