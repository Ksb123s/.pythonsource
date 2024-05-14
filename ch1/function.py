#%%
# 함수
# def 함수명(매개변수):
#     문장
#     문장
# %%
def hello():
    print("Hello!")
hello()
# %%
def add(a, b):
    return a+b

add(4,5)
# %%
def sub(a,b=3):
    return a-b

print(sub(9,5))
print(sub(9))
# %%

# 가변 : 입력값이 몇개인지 모르는 경우 사용
# 입력값을 모아 튜플로만듬
def add_many(*args):
    print(args)

add_many(1,2,3)
add_many(1,2,3,4,5,6,7)
add_many("35","24","65","98")
add_many({"dessert":"Macatoon","wine":"marlot"})
# %%
def add_many(*args):
    result =0
    for i in args:
        result += i
    return result

print(add_many(1,2,3))
print(add_many(1,2,3,4,5,6,7))
# %%
# 일반 파라메터와 가변 파라메터가 섞일때 가변파라메터를 맨 뒤에 선언
def add_many(choice, *args ):
    if choice == "add":
        result =0
        for i in args:
            result += i
    elif choice == "mul":
        result =1
        for i in args:
            result *= i
    return result

print(add_many("add",1,2,3))
print(add_many("mul",1,2,3,4,5,6,7))
# %%
# 키워드 파라메터 : kwargs
# 입력값을 모아 딕셔너리로만듬
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(name ="foo", ages=3)
print_kwargs(name ="foo", ages=3, addr="seoul")
# %%
# 일반, 가변 ,키워드 파라메터 섞이는 경우
def print_kwargs(arg1, arg2, *args,**kwargs):
    print(arg1, arg2, args,kwargs)

print(10,20)
print(10,20, "park", "kim")
print(10,20, "park", "kim", age=25, name="choi")

# %%
# 리턴값에 여러 개를 작성할 수 있는데 내부적으로는 튜플 하나로 리턴이 되는것
def add_and_mul(a,b):
    return a+b, a*b
hap, mul = add_and_mul(5,6)
print(hap, mul)
print(add_and_mul(3,4))
# %%
def func_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return [y1, y2, y3]

print(func_mul(100))
# %%
def say_nick(nick):
    if nick == "바보":
        return
    print(f"나의 별명은 {nick} 입니다.")

say_nick("바보")
say_nick("야호")
# %%
def carculater(op, num1, num2):
    result = 0
    if op =="+":
        result = num1 + num2
    elif op =="-":
        result = num1 - num2
    elif op =="*":
        result = num1 * num2
    elif op =="/":
        result = num1 - num2
    print(f"{num1} {op} {num2} = {result}")

num1 = int(input("숫자를 입력해 주세요 :"))
num2 = int(input("숫자를 입력해 주세요 :"))
op = input("안산자 입력 (+, /,*,-) :")

carculater(op, num1, num2)


# %%
a = 1
def  vartest(a):
    a = a+1
vartest(a)
print(a)
# %%
a = 1
def  vartest(a):
    a = a+1
    return a
a = vartest(a)
print(a)
# %%
a = 1
def  vartest():
    global a
    a = a+1

vartest()
print(a)
# %%
# 1~100 자리 수중에 소수에 해당하는 숫자를 찾아 리스트에 담기
primes = []
def Primes(x):
    for num in range(2, x):
        if x % num == 0:
            return False
    return True
for j in range(1,101):
    if Primes(j):
        primes.append(j)

    
       

primes


    # %%
