# 文字列メモ
print(r"C:\name\name")  #rで\n使える

print("""\
    line1
    line2\
    """)

print("Hi"*3)

s = ("aaaaaa"
     "d"
     "bbbbbb")
print(s)

word = "python"
word = "j" + word[1:]
print(word)

print(s.startswith("a"))
print(s.find("d"))          # dのインデックス探す
print(s.replace("a","c"))

print("a is {0} {1}".format("test1","test2"))
print("a is {b} {c}".format(c="test1",b="test2"))
b,c = "test2", "test1"
print(f"a is {b} {c}")      # formatと同じ

