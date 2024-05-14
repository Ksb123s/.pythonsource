# %%
# 숫자 , 문자열
# 데이터 모임 표현 list(==ArrayList(배열)), dict(==Map) ,set(==HashSet)
# %%
# 리스트 생성
list1 = []
list2 = [1,2,3,4,5,6]
list3 = [1,"a",3,"b",5,6]
list4 = [1,2,3,4,5.5,6.5]
list5 = [1,2,3,4,["Life", "is", "short"]]
list6 = list([2,3,4])
# %%
# 출력
print(list2)
# %%
# 리스트 인덱싱 / 슬라이싱
print(list2[2])
print(list3[-2])
print(list4[-1])
print(list5[-1])
print(list5[4])
print(list5[4][0])
print(list5[4][2])
# %%
list7 = [1,2,3,4,["a", "b", ["Life", "is"]]]
print(list7[4][2][1])
print(list7[-1][-1][-1])
# %%
print(list2[2:4])
print(list2[:4])
print(list2[:])
# %%
print(list5)
print(list5[4:])
print(list5[4][:2])

# %%
# 연산자
#  +
print(list2+ list3)
print(list5+ list6)
print(list2[1]+ list3[0])
# %%
# *
print(list2*2)

# %%
# len 길이
len(list2)
# %%
# 리스트 수정 / 삭제
list2[0] = 7
print(list2)

list2[1]= [10,11,12]
print(list2)

del list2[1]
print(list2)

del list2[2:]
print(list2)

# %%

for i in list3:
    print(i , end="\t")
# %%
numbers = [273,103,5,32,65,9,72,800,99]
# 100이상의 수 출력
for i in numbers:
    if i >= 100:
        print(i, end="\t")

# %%
# 홀수 , 짝수 구분하여 출력
for i in numbers:
    if i %2 == 0:
        print(f"짝수 {i}", end="\n")
    else:
         print(f"홀수 {i}", end="\n")

# %%
# 숫자 자릿수 출력
for i in numbers:
    print(f"{i}의 자릿수 : {len(str(i))}" ,end="\n")
# %%
# append():
list3.append(["c","d","e"])
print(list3)
# %%
# 1~100 까지 숫자 중에 짝수만 리스트 생성
even =[]
for i in range(101):
    if i %2 == 0:
        even.append(i)
print(even)
# %%
# sort()
a = [1,4,3,2]
a.sort()
print(a)

a = ["a",'b','c','f','e']
a.sort()
print(a)

a=['가', '다', '나 ']
a.sort()
print(a)
# %%
# reverse() : 리스트 뒤집기
print(list4)
list4.reverse()
print(list4)
# %%
# index()
list4.index(3)
list4.index(6)
# %%
# remove
# list4.remove(3)
# print(list4)
# list4.append(5.5)
# print(list4)
list4.remove(5.5)
print(list4)
# %%
# pop 마지막 요소 꺼내기(제거)
list4.pop(1)
print(list4)
# %%
# count() 
list4 = [12,13,14,15,14]
print(list4.count(14))
# %%
# extend(): list 확장
list4.extend([16,17,18])
print(list4)
# %%
# clear : 요소 전부 삭제
list4.clear()
print(list4)
# %%
numbers.sort(reverse=True)
print(numbers)
# %%
# 거짓의 해당 : "", [], (), {}, 0
city = ""
list8 = []
if city:
    print("비어 있지 않음")
    
else:
    print("비어있음")
if list8:
    print("비어 있지 않음")
    
else:
    print("비어있음")
# %%
fruit = ["딸기", "바나나", "사과", "배", "수박"]
# in == sql in 연산자와 동일 개념
if "딸기" in fruit:
    print("딸기 요소가 포함됨")

print("매론" not in fruit)

# %%
a_class =[70,60,55,75,92,80,85,100,87,65]
# a클래스의 평균과 총합 구하기
total =0

for i in a_class:
    total += i
avg = total/ len(a_class)
print(len(a_class))

print(f"a_ class 의 총점 {total}점 , 평균 {avg}점.")
# %%
# sum()
print(sum(a_class))
print(f"a_ class 의 총점 {sum(a_class)}점 , 평균 {sum(a_class)/ len(a_class)}점.")

# %%
# 리스트 컴프리핸션(comprehension)
numbers = []
for i in range(1, 10,):
    numbers.append(i)
numbers
# 요소 추가
# %%
numbers = list(range(1, 101))
numbers
# %%
numbers = [x for x in range(1, 101)]
numbers
# %%
a = [1,2,3,4]
# a라는 리스트요소에 *3을 한후 결과를 새로운 리스트에 돌려받기
result = []
for num in a:
    result.append(num*3)

result
# %%
b = ["갑", "을", "병", "정"]
# 리스트에서 정이라는 요소를 제외하고 새로운 리스트로 돌려받기
result =[]

for str1 in b:
    if str1 == "정":
        continue
    result.append(str1)
result

# %%
result = [x for x in b if x != "정"]
result
# %%
a= [1,2,3,4]

result =[x*3 for x in a if x %2 == 0 ]
result
# %%
result3 = [x for x in range(1,101) if x %2 != 0 ]
result3
# %%
list1 = ["nice", "study", "python", "anaconda", "!"]

result3 = [txt for txt in list1 if len(txt) >=5  ]
result3
# %%
list2 = ["A", "b", "c", "D", "e", "F", "G", "h"]

result4 = [alpha for alpha in list2 if alpha.islower()]
result4
# %%
a = [1,2,3,4]
b = [0,1,2,3,4]
aresult = [num*2 for num in a ]
bResult = [num1*num1 for num1 in b]

print(aresult)
print(bResult)
# %%
parking_lot= []
top, car_name = 0, "A"
while True:
    no =  int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))

    if no <=3:
        if no ==1:
            if top >= 5:
                print("주차장 꽉 찼음")
                continue
            parking_lot.append(car_name)
            car_name = chr(ord(car_name) + 1)
            top += 1
            print(parking_lot)
        elif no ==2:
            parking_lot.pop()
            print(parking_lot)
            top -=1
            car_name = chr(ord(car_name) - 1)
        else:
            print("프로그램 종료")
            break
    else:
        print("번호를 확인해 주세요 .")
# %%
# ord() : 특정 문자열 유니코드 반환
print(ord("A"))
print(chr(65))
# %%
list1 = ["body", "foo", "bar"]

for x in enumerate(list1):
    print(x)

for idx, value in enumerate(list1, start=1):
    print(idx, value)
# %%
