# filter(function , list )
# filter (fun , list ) ---> return True
mylist = [2,3,9,8,18,99,20]
print(mylist)

even_num = list (filter(lambda x : x % 2 == 0 , mylist ))
print('even_number =', even_num)

odd_num = list (filter (lambda x : x % 2 != 0 , mylist ))
print('odd_number =', odd_num )