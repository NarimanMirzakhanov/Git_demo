my_dict = {
    'name': 'Anna',
    'last_name': 'Pavlova',
    'age': 30,
    'department': 'IT'
}
print(my_dict)
# {'name': 'Anna', 'last_name': 'Pavlova', 'age': 30, 'department': 'IT'}
print(id(my_dict))
# 4300248000
print(my_dict['last_name'])
# Pavlova
my_dict['last_name'] = 'Smirnova'
print(my_dict)
# {'name': 'Anna', 'last_name': 'Smirnova', 'age': 30, 'department': 'IT'}
print(len(my_dict))
# 4
my_dict['salary'] = 5000
print(my_dict)
# {'name': 'Anna', 'last_name': 'Smirnova', 'age': 30, 'department': 'IT', 'salary': 5000}
print(len(my_dict))
# 5
print(my_dict.keys())
# dict_keys(['name', 'last_name', 'age', 'department', 'salary'])
print(my_dict.values())
# dict_values(['Anna', 'Smirnova', 30, 'IT', 5000])
print(my_dict.items())
# dict_items([('name', 'Anna'), ('last_name', 'Smirnova'), ('age', 30), ('department', 'IT'), ('salary', 5000)])
print(my_dict.pop('salary'))
# 5000
print(my_dict)
# {'name': 'Anna', 'last_name': 'Smirnova', 'age': 30, 'department': 'IT'}
print(my_dict.get('salary'))
# None
print(my_dict.get('salary', 'Not found'))
# Not found
key = ['name', 'salary', 'department']
values = ['Alex', 50000, 'HR']
employee = dict(zip(key, values))
print(employee)
# {'name': 'Alex', 'salary': 50000, 'department': 'HR'}
employee1 = dict(name='John', position='developer', salary=20000, department='IT', city='NY')
print(employee1)
# {'name': 'John', 'position': 'developer', 'salary': 20000, 'department': 'IT', 'city': 'NY'}
employee2 = dict([['name', 'Mike'], ['position', 'tester'], ['salary', 6000], ['department', 'IT'], ['city', 'SF']])
print(employee2)
# {'name': 'Mike', 'position': 'tester', 'salary': 6000, 'department': 'IT', 'city': 'SF'}

dct = {
    'USA': '+1',
    'Russia': '+7',
    'Turkey': '+90'
}
print(*dct, sep='\n')
# USA
# Russia
# Turkey

dct1 = {
    'name': 'Anna',
    'age': 19
}
dct3 = dct | dct1
print(dct3)
# {'USA': '+1', 'Russia': '+7', 'Turkey': '+90', 'name': 'Anna', 'age': 19}
for key in dct:
    print(key)
# USA
# Russia
# Turkey

for key in dct.keys():
    print(key)
# USA
# Russia
# Turkey

for key in dct:
    print(dct[key])
# +1
# +7
# +90

for value in dct.values():
    print(value)
# +1
# +7
# +90

for key, value in dct.items():
    print(key, value)
# USA +1
# Russia +7
# Turkey +90

print(dct.setdefault('France', '+33'))
# USA +1
# Russia +7
# Turkey +90
# +33

print(dct)
# {'USA': '+1', 'Russia': '+7', 'Turkey': '+90', 'France': '+33'}

print(dct.pop('Turkey'))
# +90
print(dct)
# {'USA': '+1', 'Russia': '+7', 'France': '+33'}
keys = list(dct.items())
print(keys)
# [('USA', '+1'), ('Russia', '+7'), ('France', '+33')]

print(dct.popitem())
# ('France', '+33')
print(dct)
# {'USA': '+1', 'Russia': '+7'}
print(dct.popitem())
# ('Russia', '+7')
print(dct)
# {'USA': '+1'}

