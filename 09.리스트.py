# appen,del,len,[start,end,step]

company_list = ["삼성", "애플", "LG"]

print(company_list[0])
# 재할당
company_list[2] = "테슬라"
# 추가
company_list.append("아마존")
# 삭제
del company_list[0]
# 길이
print(len(company_list))
# 슬라이싱
print(company_list[0:2])
print(company_list[:1])
print(company_list[::2])
