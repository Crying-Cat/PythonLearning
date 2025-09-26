def mydecorator(function):
    def wrapper(*args,**kwargs):
        print("my decorator")
        return function(*args,**kwargs)
    return wrapper

@mydecorator
def hello_world(name):
    print(f"Hello world {name}")
    return f"Hello world {name}"

hello_world("mike")
# mydecorator(hello_world)("mike")

#Example 1:
def logged(function):
    def wrapper(*args,**kwargs):
        value = function(*args,**kwargs)
        with open('logfile.txt','a+') as f:
            fname = function.__name__
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper


@logged
def add(a,b):
    return a+b

add(1,2)
# logged(add)(1,2)

#Example 2
import time
def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} takes {after - before} second to execute")
        return value
    return wrapper

@timed
def myfunction():
    time.sleep(1)
    return None

myfunction()
# timed(myfunction)()