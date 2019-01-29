# matrix 3*4
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

m10 = matrix[2][1]
m8 = matrix[1][3]
print(m10 , m8)

# tranpose matrix 4*3
transpose = []
for i in range(4):
    transpose.append([row[i] for row in matrix])

print(transpose)

# another way
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)

# build-in function zip() ---- transpose matrix
transpose = list (zip(*matrix))
print(transpose)