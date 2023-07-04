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

d = {'x':10,'y':20}
d['x'] = "XXXX"
d["z"] = 200
d[1] = 10000
print(d['x'],d)

d.keys()        # keyだけ取り出し
d.values()      # valueだけ取り出し
d2 = {'x':1000,'j':500}
d.update(d2)    # 更新
print(d)
d.pop("x")
del d["y"]
print(d)
d.clear()
print(d)
d = {"a":100,"b":200}
print("a" in d)

# 参照渡し
x = {"a":1}
y = x
y["a"] = 1000
print(x,y)      
# 値渡し
x = {"a":1}
y = x.copy()
y["a"] = 1000
print(x,y)   


a = {1,2,2,3,4,4,5,6}
print(a,type(a))
b = {2,3,3,6,7}
print(a-b)
print(a&b)      # 論理和
print(a|b)      # 論理積
print(a^b)      # 排他

s = {1,2,3,4,5}
s.add(6)
s.add(6)
s.remove(5)
print(s)
s.clear()
print(s)

f=["apple","banana","apple","banana"]
kind=set(f)
print(kind)

