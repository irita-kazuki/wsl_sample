# データ構造
n=[1,2,3,4,5]
print(n[::2],n[::-1])

s=["a","b","c","d","e"]
s[2:4] = []             # リスト要素消す
print(s)

n.insert(0,200)
print(n)
n.pop(1)                # リスト要素消す
print(n)
del n[2]
print(n)

r=[1,2,3,4,5,1,2,3]
r.sort(reverse=True)
print(r)

#　値渡し(int)
i0 = 10
j0 = i0
j0 = 100
print(j0,i0)
print(id(j0),id(i0))
#　参照渡し(リスト要素)
i1=[1,2,3,4,5]
j1 = i1           
j1[0] = 100
print(j1,i1)
print(id(j1),id(i1))
#　値渡し(リスト要素)
i2 =[1,2,3,4,5]
j2 = i2.copy() 
j2[0] = 100
print(j2,i2)
print(id(j2),id(i2))

num_tuple = (10,20)
x, y = num_tuple    # 変数をタプルから代入
print(x,y)
x,y = y,x           # 2変数の入れ替え
print(x,y)
