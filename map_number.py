# x>10 ---> 'big'   x<10 ---> 'small'
numbers = [12,9,55,7,18,20,5,3,48]
print(numbers)

out = list(map(lambda x : 'big' if x>10 else 'small' , numbers ))
print(out)

