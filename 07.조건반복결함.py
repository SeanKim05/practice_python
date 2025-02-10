while True:
    order = input("명령을 내려주세요")
    if order == "go":
        print("계속진행")
    elif order == "stop":
        print("종료")
        break
    else:
        print("잘못입력")
