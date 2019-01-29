# yield ---> return , function remeber next output

def firstn():
    yield 1
    yield 2
    yield 3

for i in firstn() :
    print(i)

# num ++ 
def Firstn(n):
    num = 0
    while (num < n ):
        yield num
        num += 1

for i in Firstn(10):
    print(i) 

print(Firstn(10))