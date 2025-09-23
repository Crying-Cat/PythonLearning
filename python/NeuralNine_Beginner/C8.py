#出错处理
try:
    a = input("input a number: ")
    b = input("input a number: ")
    print(int(a)/int(b))
except:
    print("Error")
finally:
    print("程序结束")

#特定错误处理
try:
    a = input("input a number: ")
    b = input("input a number: ")
    print(int(a)/int(b))
except ValueError:
    print("请输入数字")
except ZeroDivisionError:
    print("除数不能为0")
finally:
    print("程序结束")

#打印错误信息
try:
    a = input("input a number: ")
    b = input("input a number: ")
    print(int(a)/int(b))
except Exception as e:
    print(e)
finally:
    print("程序结束")


def function(a):
    if type(a) is not int:
        # raise Exception("a must be int")
        raise TypeError("a must be int")
    print(a)

function(5)
try:
    function("5")
except Exception as e:
    print(e)
input("Press Enter to continue...")


try:
    assert 1>2, "1不大于2" #assert后面是条件，条件不成立则抛出异常
except Exception as e:
    print(e)

