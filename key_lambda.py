#a = [(x,y) for x in [] for y in range(5) if not x==y ]
a = [(3,5),(7,8),(9,2),(6,4)]
print(a,len(a))

# key lambda function for sort method

# a.sort() eval x[0]
a.sort(key = lambda x : x[0])
print(a)

a.sort(key = lambda x : x[1])
print(a)
