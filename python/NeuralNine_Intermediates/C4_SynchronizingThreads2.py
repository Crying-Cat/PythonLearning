import threading
import time


semaphore = threading.BoundedSemaphore(value=5)

def access(thread_index):
    # global semaphore
    print(f"thread{thread_index}: is trying to access")
    semaphore.acquire()
    print(f"thread{thread_index}: is accessing")
    time.sleep(10)
    print(f"thread{thread_index}: is releasing")
    semaphore.release()
    pass

for thread_index in range(1,11):
    t = threading.Thread(target=access,args=(thread_index,))
    t.start()
    time.sleep(0.51)
