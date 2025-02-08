# 자료형
# string, boolean, float, int

# 형 변환 str() 문자 float() 실수 int() 정수
a = int("100")
b = float("10.12")
c = str(123)
print(type(a), type(b), type(c))

# 문자열 연산 * 0 : 사라짐, *소수점 : 계산안됨
print("100" * 2)

name = input("이름")
count = int(input("tn"))

print(name * count)
