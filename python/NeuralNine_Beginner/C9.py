# 手动关闭文件
file = open("./files/file.txt","r")
print(file.read())
file.flush() # 刷新文件
file.close() # 关闭文件

# 自动关闭文件
with open("./files/file.txt","r") as file:
    print(file.read()) #读取文件
    file.seek(0) # 光标回到开头
    print(file.readlines()) #读取文件的所有行
    file.flush() # 刷新文件


# 文件写入
with open("./files/file2.txt","w") as file:
    file.write("Hello World!\n")
    file.write("wyj!\n")

with open("./files/file2.txt","r") as file:
    print(file.read()) #读取文件

# 追加写入
with open("./files/file2.txt","a") as file:
    file.write("new addin\n")

import os

# 创建目录 
if not os.path.exists("newdir"):
    os.mkdir("newdir")
os.chdir("newdir") #修改当前文件夹
if not os.path.exists("newdir1"):
    os.mkdir("newdir1")

# 重命名文件
os.chdir("../")
os.rename("files/file.txt","files/file1.txt")

# 创建文件
# try:
#     with open("./files/file3.txt","x") as file:
#         file.write("Hello World!\n")
#         file.write("wyj!\n")
# except FileExistsError:
#     print("文件已存在")
# finally:
#     print("程序结束")