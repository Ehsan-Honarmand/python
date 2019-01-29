word = ['salam','ehsan','age 27 years old'] 
for i in word:
    print(i,len(i))

# Loop over a slice copy of the entire list.
for w in word[:]:
    if len(w)>6:
        word.insert(0,w)

for i in word:
    print(i,end=',')
    