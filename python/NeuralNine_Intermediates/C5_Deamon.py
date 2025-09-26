import threading
import time

path = 'text.txt'
text = ''

lock = threading.Lock()

def readFile():
    global path,text
    while True:
        with open(path) as f:
            lock.acquire()
            text = f.read()
            lock.release()
            time.sleep(3)

def printloop():
    for x in range(5):
        lock.acquire()
        print(f"{x}:{text}")
        lock.release()
        time.sleep(1)

if(True):
    t1 = threading.Thread(target=readFile,daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()