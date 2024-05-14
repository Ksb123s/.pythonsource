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
str1 = "파이썬프로그래밍"
for s in str1:
    print(s, end="❤")
# %%
# 사용자로 부터 숫자를 입력받고 
num1 = input("숫자를 입력해 주세요")

for i in range(len(num1)):
    print()
    for j in range(int(num1[i])):
        print("❤", end="")
           

# %%
# 문자열 함수
# count() : 문자열에 포함된 특정 문자열 개수 
str1= "hobby"
print("a 문자열에 포홤된 b의 개수 %d"% str1.count("b"))

# %%
# find() : 특정 문자  위치
str1 = "Python is the best choice"
print("a 문자열의 b 위치 %d" % str1.find("b"))
print("a 문자열의 b 위치 {}" .format( str1.find("b")))
print(f"a 문자열의 b 위치 {str1.find("b")}" )
print(f"a 문자열의 b 위치 ",str1.find("b") )
# %%
# index() :문자열 위치
print("a 문자열의 b 위치 %d" % str1.index("b"))
# %%
# find() 와 index() 차이
print("a 문자열의 b 위치 %d" % str1.index("k")) 
# index 찾지 못하면 오류 발생 -ValueError
print("a 문자열의 b 위치 %d" % str1.find("k"))
# find 찾지 못하면 -1

# %%
# startswith / endswith
str2 = "Python Is Easy Programming"

print(str2.startswith("P"))
print(str2.endswith("P"))

# %%
# join()
",".join("asdfgre")
# 리스트나 튜플 문자열로 변경 시 많이 사용됨
list1 = ["a","b","c","d","e"]
print(",".join(list1))
# %%
# upper, lower/ swapcase/ title : 대소문자 변경
a="abcdef"
print("소 => 대 ", a.upper())
a="ABCDEF"
print("대 => 소 ", a.lower())
a = "Python is Easy"
print("대문자 소문자 상호 변환", a.swapcase())
a = "python is easy"
print("단어의 제일 앞글자 대문자 변환", a.title())
# %%
# Python 대소문자 구별 함
"abc" == "ABC"
# %%
# lstrip/rstrip/strip : 공백 제거
a = "       hi          "
print(a)
print("left strip",a.lstrip())
print("right strip",a.rstrip())
print("strip",a.strip())
# %%
# replace
a= "Life is too short"
a.replace("Life", "Your leg")
# %%
# split() : 문자열 나누기
print(a.split()) # 공백 기준
b = "a:b:c:d"
print(b.split(":"))
# %%
# splitlines() :enter 기준 나누기
c= "하나\n둘\n셋"
print(c.splitlines())
# %%
#  is~ : True,False 로 결과 (문자열 의 구성 파악)
print("12345".isdigit())
print("abcd".isalpha())
print("abc123".isalnum())
print("abcd".islower())
print("ABCD".isupper())
print("   ".isspace())
# %%
# 대 <=> 소
name = "KennRy"
print(name.swapcase())

# %%
# 년월일 입력 받은 후 10년후 날짜 출력
# 입력(2024/05/13)ex
yyddMM = input("년일월을 입력해 주세요 ex)2024/05/24")
yy= int(yyddMM[0:4])

newYYddMM = yyddMM.replace(str(yy) ,str(yy+10))
print(f"10년후 날짜는 {newYYddMM}")

# %%
# 사이트별 비밀번호 작성
# https//:naver.com
# 1. https// 제외
# 2. 처음 나오는 . 이후 부분 제외
# 3. 남은 글자중처음 세자리+ 글자개수 + 글자내 e 문자수 +"!"

str1  = " https//:naver.com"
str2 = str1.replace("https//:", "")
str2 = str2[: str2.find(".")]
pwd =  str(str2[1:4]) + str(len(str2)) +str(str2.count("e")) + "!"
print(pwd)
# %%
