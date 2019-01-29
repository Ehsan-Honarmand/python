# map (function , list)
mylist = [2,5,6,8,11]
print(mylist)

M = list(map(lambda x : x*2 , mylist))
print(M)

M = list(map(lambda x : x*'sos' , mylist))
print(M)