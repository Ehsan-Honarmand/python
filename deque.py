from collections import deque
q = deque(['ehsan','samira','saeed'])

q.append('mohsen')
q.append('mohadese')

q.popleft() # ehsan leave
print(q)
q.popleft() # samira leave

print(q)