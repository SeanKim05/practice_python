# for i in range(5):
#     for j in range(5 - i):
#         print("*", end="")
#     print()


for i in range(5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(2 * (i + 1) - 1):
        print("*", end="")
    print()
