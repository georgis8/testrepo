


limit = 20
values =[3,5]
    
multiples=[]
for value in values:        
    for number in range(value,limit,value):
        multiples.append(number)
  
print(sum(set(multiples)))

numbers = list(range(values[1],limit,values[1]))

def sum_of_m(limit,multiples):
    return sum({x for m in multiples if m != 0 for x in range(m, limit, m)})