# 연산자
a, b = 5,3

print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
a+=5
print(a)
a*=5
print(a)
a%=5  
print(a)


money, c500, c100,c50,c10 = 0,0,0,0,0
money = 7777

c500 = money//500
c100 = (money- 500*c500)//100
c50 = (money- 500*c500 - 100*c100)//50
c10 = (money- 500*c500 - 100*c100 - c50*50)//10
money = (money- 500*c500 - 100*c100 - c50*50 - c10*10)
print("500원 {}개 , 100원 : {}개 , 50원 : {}개 , 10원 : {}개, 나머지 {}원".format(c500, c100, c50,c10 ,money))



# 관계연산자 > , < , <=, >= , != ,==

a,b = 10,5
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a < b)
print(a > b)

# 논리 연산자 and or not
a,b,c = 100,50,10
print("논리연산자\n")
print("or : ",a > b or c< b)
print("and : ",a > b and c< b)
print("not : ",not a > c)
print("not : ",not True)
print("not : ",not False)


# 사망연산자 사용하지 않음
print("사망연산자 대체\n")
str = "안녕하세요" if True else "반갑습니다."
print(str)


