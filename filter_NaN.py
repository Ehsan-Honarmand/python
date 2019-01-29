import math 
value = [12.3,2.33,float('nan'),3.66,6.22,float('nan')]

filtered_data = []
for i in value :
    if not math.isnan(i):
        filtered_data.append(i)

print(filtered_data)
