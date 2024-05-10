#%%
# while : for
# ++ --
i = 1
while i< 11:
    print(i)
    i = i+1
# %%
# 1~100 짝수만 출력
i = 1
while i < 101:
    if i %2 ==0:
        print(i, end=" ")
    i +=1
# %%
# 1~100까지 합게
i = 1
sum1 = 0
while i < 101:
    sum1 += i
    i += 1
print(sum1)
# %%
# 6단 구구단
i = 1
while i <10:
    print(i*6)
    i+= 1

# %%
#  사용자에 겡입력 받은 후 출력
# q 입력시 입력 받는것 중단
while True:
     msg = input("아무거나 입력 q => 종료")
     if msg == "q":
         break
     print(msg)
# %%
# for 변수명 in 범위 :
range(5)
print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,11,2)))
# %%
for i in range(10):
    print(i , end=" ")

# %%
for i in range(1,11):
    print(i , end=" ")
# %%
for i in range(1,101, 2):
    print(i , end=" ")

# %%
#  1~100 합계
sum1 = 0
for i in range(1,101):
    sum1 +=i
sum1
# %%
# sum()

print(sum(range(1,101)))
print(sum(range(1,101,2)))

# %%
# 1 부터 사용자 입력수 까지 합계
num1 = int(input("숫자 입력"))
sum1 = 0
sum1 = sum(range(1,num1))
sum1
# %%
for s in "dreams":
    print(s)

# %%
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
# %%
for i in range(2, 10):
    for j in range(1,10):
        print("{} * {} = {}".format(i, j, i*j) , end="\t")
    print()
# %%
# 리스트 ==> qoduf
numbers = [4,3,1,4,51,24,17,2,33,15,34,68]
for num in numbers:
    print(num)
# %%
#  break
i =1
while i <11:
    if i ==5:
        break
    print(i , end=" ")
    i+= 1
# %%
i =1
while i <11:
    i+= 1
    if i %2 ==1:
        continue
    print(i , end=" ")
    
# %%
