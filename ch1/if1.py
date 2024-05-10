#%%
if True:
    print(111)
# %%
a= 200

# a 가 100보다 크고 200보다 작거나 같은지 확인
if a > 100 and a<=200:
    print("a는 100보다 크고 200보다 작거나 같다")
# %%
if 100< a<=200:
    print("a는 100보다 크고 200보다 작거나 같다")
# %%
# a b c 중 가장 큰수 출력
a,b,c = 12,6,18
max = a
if max<b:
    max = b
if max< c:
    max = c
print(max)
# %%
if True:
    print("True")
else:
    print("False")
# %%
score, grade = 90, "A"
if score >= 90 and grade =="A":
    print("합격")
else:
    print("불합격")
# %%
# 입력받은 숫자 짝 홀 구분
num1 = int(input("숫자를 입력해 주세요"))

if (num1 % 2) == 0:
    print("짝수")
else:
    print("홀수")

# %%
# 중첩 if
a = 75
if a>50:
    if a< 100:
        print("50보다 크고 100 보다 작다")
    else:
        print("100보다 크다")
else:
    print("50보다 작다")
# %%
# 다중 if
# elif
num = 90
if num >=90:
    print("A")
elif num >=80:
    print("B")
elif num >=70:
    print("C")
elif num >=60:
    print("D")
else:
    print("f")
# %%
# age height 입력 받은후
#age 가 20 이상이고 hight 가 170 이상이라면 : a 지망 지원가능
#age 가 20 이상이고 hight 가 160 이상이라면 : b 지망 지원가능
#age 가 20 이상이고 hight 가 160 미만이라면 : 지원 불가
#age 가 20 미만이라면 : 20세 이상 지원가능
age = int(input("나이 입력해 주세요"))
height = int(input("키를 입력해 주세요"))
if age >= 20 and height >=170 :
    print("a 지망 지원가능")
elif age >= 20 and height >=160 :
    print("b 지망 지원가능")
elif age >= 20 and height <160 :
    print("지원 불가")
elif age < 20  :
    print("20세 이상 지원 가능")
# %%
# 81 ~100 a학점
# 61 ~80 b학점
# 41 ~60 c학점
# 21 ~40 d학점
# 0 ~20 e학점
score = int(input("점수를 입력해 주세요"))
if 81<=score <=100 :
    print("a 학점")
if 61<=score <=80 :
    print("b 학점")
if 41<=score <=60 :
    print("c 학점")
if 21<=score <=40 :
    print("d 학점")
if 0<=score <=20 :
    print("e 학점")

# %%
# 두개 숫자 입력 , 연산자 입력후 계산해서 출력

num1 = int(input("첫번째 숫자를 입력해 주세요"))
num2 = int(input("두번째 숫자를 입력해 주세요"))
op = input("연산자 입력해 주세요 +,/,*,-,//,**,%")

match op:
    case "+":
        print("{} {} {} = {}".format(num1, op, num2, (num1 +num2)))
    case "/":
        print("{} {} {} = {}".format(num1, op, num2, (num1 /num2)))  
    case "*":
        print("{} {} {} = {}".format(num1, op, num2, (num1 *num2)))
    case "-":
        print("{} {} {} = {}".format(num1, op, num2, (num1 -num2)))
    case "//":
        print("{} {} {} = {}".format(num1, op, num2, (num1 //num2)))
    case "**":
        print("{} {} {} = {}".format(num1, op, num2, (num1 **num2)))
    case "%":
        print("{} {} {} = {}".format(num1, op, num2, (num1 %num2)))
# %%
