#%%
# set (집합)
# 중복을 허용하지 않음 / 순서 x
set1 = set()
set2 = set([1,2,3,4])
set3 = set([1,4,5,6,6])
# %%
print(set3)
print(set2)
# %%
# 리스트나 튜플로 전환 : 인덱시이 필요하다면
# list(), tuple()
list1 = list(set2)
t1 = tuple(set3)
print(list1)
print(t1)
# %%
dict1 = {"no":1, "name" : "hong", "age" : 25}
set(dict1)
# %%
list1 = [1,2,3,4,5]
set(list1)
# %%
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))



# %%
# add : 추가
s1.add(7)
s1
# %%
# update() : 어러개 추가
s1.update([9,10,11])
s1
# %%
# remove: 제거
s1.remove(2)
s1
# %%
