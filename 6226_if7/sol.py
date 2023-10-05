numbers = range(1, 201)

result = []

for i in numbers:
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))    
        
print(','.join(result))