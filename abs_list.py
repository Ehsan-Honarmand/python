vec = [-1 , -2 , -3 , 0 , 1 , 5]
# x = vec * -1
x = [i*-1 for i in vec ]
print(x)

#filter negative
y = [i for i in vec if i>=0]
print(y)

#abs of list
z = [abs(i) for i in vec ]
print(z)

z_one = [i for i in z if i != 1 ]
print(z_one)