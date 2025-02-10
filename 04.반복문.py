# for 변수 in range
for i in range(5):
    print(i)

# # 복합 할당 연산자 += -+ *= /=
num = int(input("더할 수"))
res = 0
for i in range(1, num):
    res += i
print(res)

# range의 활용
# range(start, end) 1,6 -> 1,2,3,4,5
# range(start, end, step) 1,11,2 -> 1, 3, 5, 7, 9 / 5,0,-1 -> 5,4,3,2,1

# while
# 초기식
# while 조건식:
# 반복
#  증감식
x = 0
while x < 10:
    print("heeello")
    x += 1

start = int(input())
end = int(input())
sum = 0
for i in range(start, end + 1):
    sum += i
print(sum)

y = 1
while i < 11:
    print(i)
    i += 2

startIdx = int(input("몇 단?"))
for i in range(1, 10):
    print(f"{startIdx} * {i} = {startIdx * i}")
