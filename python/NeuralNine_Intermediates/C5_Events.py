import threading

event = threading.Event()

def function():
    while(True):
        event.wait()
        print("evnet is Triggled")
        event.clear()

t = threading.Thread(target=function)
t.start()

while(True):
    s = input("(y/n?)")
    if s == 'y':
        event.set()

