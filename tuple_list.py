Tul = [(x,y) for x in range(10) for y in range(10) if x != y]
print(Tul)

tul_i = Tul.index((3,7))
print(tul_i, Tul[tul_i])

x = [i**2 for i in range(10)]
print(x)
# x =[]
# for i in range(10):
#       x.append(i**2)
