#%%
# 문자 처리
# 문자, 문자열 구분 안함 -쌍따음표, 홀따옴표 허용 3개
# "Life us too short, You Need Python"
# 'Life us too short, You Need Python'
# '''Life us too short, You Need Python'''
# """Life us too short, You Need Python"""

multiline = '''
    Life us too short
     You Need Python
'''
multiline
# %%
str1 = "Python"+ "is fun"
str1
# %%
"Python"*2
# %%
print("=" *50)
print("My Python" )
print("=" *50)
# %%
# 문자열 인덱싱과 슬라이싱
print(str1[3])
print(str1[5])
print(str1[-1]) # 오른쪽에서 인덱싱
# %%
# 슬라이싱 [시작위치: 끝위치] => 끝위치 포함 안함
str1 = "Life us too short"
print(str1[0:1])
print(str1[0:4])
print(str1[4:])
print(str1[4:8])
print(str1[:17])
print(str1[0:-4])

# %%
# 길이 함수 len()
len(str1)

# %%
str2 = "20240510Sunny"
# 년월일 출력
date= str2[:8]
print(str2[:8])
# 날씨 출력
weather = str2[8:]
print(str2[8:])


# %%
print(str2[:4] +"-"+ str2[4:6] +"-"+str2[6:8])
# %%
jumin="901205-3234567"
# 주민 등록 번호 에서 1 or 3 남자, 2 or 4 여자
if jumin[7] == "1" or jumin[7] =="3":
    print("남자")
elif jumin[7] == "2" or jumin[7] == "4":
    print("여자")

# %%
