# if 조건문: 들여쓰기 4칸
origin_pwd = "1234"
input_pwd = input("비밀번호 입력")
if origin_pwd == input_pwd:
    print("로그인 성공")
elif input_pwd == "":
    print("입력해라 비번")
else:
    print("틀린 비밀번호")
print("종료")  # if문을 벗어나고 실행

subscriber = int(input("현재 구독자 수"))
if subscriber >= 1000:
    print("수익창출 가능")
else:
    print("수익 창출 불가능")
