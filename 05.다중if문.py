# and,or,not 입력
# sub_count = int(input("구독자 수"))
# watch_time = int(input("시청시간"))

# if sub_count >= 1000 and watch_time >= 4000:
#     print("수익 창출 가능")
# else:
#     print("수익 창출 불가능")


write = int(input("필기점수"))

if write > 80:
    interview = input("면접결과")
    if interview == "pass":
        print("최종합격")
    elif interview == "fail":
        print("불합격")
else:
    print("불합격")
