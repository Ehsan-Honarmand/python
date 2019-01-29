from collections import deque
q = deque(range(10))
print(q)
for i in range(1,10):
    q.appendleft(-i)

print(q)
q.insert(q.index(0),[])
print(q)
