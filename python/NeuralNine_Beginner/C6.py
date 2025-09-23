mylist = [10,20,30,300,"String"]
print(mylist)

# 改
mylist[0] = 100
mylist[1:3] = [200,300]
print(mylist)

# 查
print(mylist[0])
print(mylist[-1])
print(mylist[0:3])
print(mylist[1:3])
print(mylist[:3])
print(mylist[3:])

for item in mylist:
    print(item)

index = mylist.index(300) # 查找300的下标
print(index)

print(300 in mylist) # 判断300是否在列表中

# 增
list = mylist
list.append(40)
list.insert(1,15)
list.insert(1,15)
print(mylist)

# 删
list.remove(15) # 删除第一个15
list.pop() # 删除最后一个元素
list.pop(2) # 删除下标为2的元素
print(mylist)

# 其他操作
print(mylist + [400,500])
print(mylist*4)

print(len(mylist))
print(max(mylist[0:3]))
print(min(mylist[0:3]))

# 排序
x = [2,5,6,2,0,8,9,1,4,7,3]

print(sorted(x))
print(x)

x.sort()
print(x)


dic = {
    "name":"张三",
    "age":20,
    20:49
}

# 改
dic["age"] = 30
print(dic)
# 查
print(dic["name"])
# 增
dic["weight"] = 70
print(dic)
# 删
del dic["age"]
print(dic)

# methods:
print(dic.keys())
print(dic.values())
print(dic.items())


