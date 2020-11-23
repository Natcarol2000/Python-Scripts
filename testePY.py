

a=['a','b','c','d', 'ax']

l=[]
x='a'
y='x'

for i in a:
    l.append(i)
    if x not in a and y not in a:
        c=x+y
    else:
        continue
        if c in a:
            l.append(c)
            print('word found:', c)
            break
        
        else:
            print('not found')

            
print(l)
