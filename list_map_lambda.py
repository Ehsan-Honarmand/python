y = []
for x in range(10):
    y.append(x*.1)

print(y)

#list_map_lambda

y = list(map(lambda x : x*.1 , range(10)))
print(y)
