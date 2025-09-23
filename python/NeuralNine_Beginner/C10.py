txt = "Hello World"

# 查
print(txt[2])
print(txt[:])
print(txt[1:2])
for l in txt:
    print(l)

print('l' in txt) #字符是否存在
print(txt.count('l')) #字符出现的次数
print(txt.index('l')) #第一个字符的索引
print(txt.find('l')) #第一个字符的索引

# 改
print(txt.replace('Hello','hallo'))
print(txt)

# 增
txt += '!'
txt += " WYJ"
print(txt)

# method
print(len(txt)) #字符串长度
print(txt.lower()) #大小写转换
#join
separator = ';'
mylist = ['Pig','Dog','Cat']
print(separator.join(mylist))
#split
text = "my name is wyj"
print(text.split(' '))

# 打印输出
name = input("input yuor name:")
age = int(input("input your age:"))
print(f"name:{name}\nage:{age}")