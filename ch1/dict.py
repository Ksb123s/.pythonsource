#%%
#dictionaly == map
# 리스트와 같이 많이 끄이는자료향
# Key: value
# {}
# %%
# 생성
dict1 = {}
dict2 ={"name": "Song", "age" : 12}
dict3 ={0: "Hello Python", 1 : "Hello Coding"}
dict4 ={"arr": [1,2,3,4,5]}
# %%
print(dict2)
print(dict3)
print(dict4)
# %%
# 특정 키의 요소 출력
print(dict2["name"])
print(dict3[0])
print(dict4["arr"])
# %%
# KeyError: 'addr'
print(dict4["addr"])
# %%
dict1.get("addr")
# %%
# 데이터 추가 - 키와 값의 형태로 추가
dict2["birth"] = "0514"
dict2
# %%
dict3[2] = ["Hello Java", "HEllo Oracle"]
dict3
# %%
# dict4 key rank: (16,17,18)
dict4["rank"] = (16,17,18)
dict4
# %%
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]

# {1 : 3, 2: 4, 6:1}
counter = {}
for i in numbers:
    counter[i] = numbers.count(i)
counter
# %%
# del 삭제 
del dict2["birth"]
dict2
# %%
# keys()
dict2.keys()
# %%
# values()
dict2.values()
# %%
# items()
dict3.items()
# %%
for k in dict2.values():
    print(k)
# %%
for k,v in dict2.items():
    print(k, v)
# %%
"name" in dict1
# %%
"name" in dict2
# %%
# clear() : 전부 지우기
dict2.clear()
dict2
# %%
q1 = {"봄" : "딸기", "여름": "토마토", "가을" : "사과", "겨울" : "귤"}

print(q1["가을"])

str = "사과가 포함됨" if"사과" in q1.values()else "사과가 포함되지 않음"
str
# %%
