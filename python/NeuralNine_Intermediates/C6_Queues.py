import queue

q = queue.Queue() #先进先出
q = queue.LifoQueue() #后进先出


q.put(1)
q.put(2)

while not q.empty():
    print(q.get())

pq = queue.PriorityQueue() #优先队列

# pq.put(12)
# pq.put(11)
# pq.put(13)
pq.put('b')
pq.put('a')
pq.put('c')
while not pq.empty():
    print(pq.get())