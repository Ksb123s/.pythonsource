#%%
# tuple : ()
#  튜플은 요소값을 바꿀수 없음(sort, remove,inset,pop 같은 함수 x)
# %%
# 생성
t1 = ()
t2 = (1,) # 요소가 1개만 을 가진다면 뒤에 쉼표 반드시 필요함
t3 = (1,2,3)
t4 = 1,2,3 # 소괄호 생략 가능
t5 = ("a","b",("ab", "cd"))
# %%
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
# %%
del t3[0]
print(t3) #TypeError: 'tuple' object doesn't support item deletion
# %%
t3[1]
# %%
t3[1:]
# %%
t6 = t1+t2
print(t6)
# %%
t6 =t3*3
t6
# %%
len(t6)
# %%
