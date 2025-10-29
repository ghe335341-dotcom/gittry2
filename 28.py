dict1={'name':'Tom','age':20,'gender':'male'}
for key in dict1.keys():
    print(key,end=' ')
for value in dict1.values():
    print(value,end=' ')
for item in dict1.items():
    print(item, end=' ')
print()
for key,value in dict1.items(): #分离元组数据（拆包）
    print(f'{key}={value}')
#oh my goodness
