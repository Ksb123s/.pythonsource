# 함수 : print(출력 문구 또는 변수 입력) == sout()
print('Hello Python!')
print("Hello Python!")
print(200)
print("200")
print(25.3)
print("25.3")
# 타입
print(type("Hello Python!"))
print(type(200))
print(type(25.3))


# print() 에 사용하는 
print("T","E","S", "T")
print("T","E","S", "T",sep="")


print("Welcome to",end=" ")
print("안녕하세요")

# 포메팅 -%d, %s,%f %c
print("%d" % 100)
print("%5d" % 100)
print("%05d" % 100)
print()
print("%s"% "hi")
print("%5s"% "hi")
print()
print("%-8.2f"% 123.21)
print("%8.2f"% 123.21)
print("%8.2f"% 123.215647)

number = 4
print("I eat %d apples" % number)

print("%d : %s" % (1, "홍길동"))

# %s : 어떤 형태의 값이든 문자열로 변환
print("I eat %s apples" % number)
print("I eat %s apples" % 3.1415)
print("I eat %s apples" % "Three")

# %% : % 기호 화면 출력
print("Errors is %d%%" %98)

print()
# format() : 포멧코드와 유사한 역할
print("i eat {} apples".format(3))
print("i eat {0} apples".format(3))
print("{} and {} ".format("you", "me"))
print("{0} and {1} and {0} ".format("you", "me"))


# formate()+ 인덱스 + 이름
print("{var1} and {var2} ".format(var1="you", var2="niceman"))
print("i eat {0} apples. so i was sick for {day} days" . format(10, day=3))

print("{0: <10}" .format("hi"))
print("{0: >10}" .format("hi"))
print("{0: ^10}" .format("hi"))
print("Test1: {0: 5d}, price: {1: 4.2f}".format(776, 6534.123))


print("\n줄바꿈\n 연습")
print("\t 텝\t 연습")
print('글자가 "강조되는" 효과')
print("글자가 '강조되는' 효과")






