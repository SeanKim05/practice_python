# nums = [5, 15, 2, -8, -12, -29, 43, 1]
# min = float("inf")
# for val in nums:
#     if val < min:
#         min = val
# print(min)

# nums = [5, 15, 2, -8, -12, -29, 43, 1]
# sum = 0
# for num in nums[::2]:
#     sum += num
# print(sum)

import random

list = []
i = 0

while i < 6:
    num = random.randint(1, 45)
    if num not in list:
        list.append(num)
        i += 1
    if i == 6:
        break

for res in list:
    print(res, end=" ")
