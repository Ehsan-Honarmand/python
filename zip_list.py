Question = ['name','years old','favorite color'] 
answer = ['ehsan','27 years old','white']

#match list with zip()
for q,a in zip(Question,answer):
    print('what is your {0} ? It is {1}'.format(q,a))

