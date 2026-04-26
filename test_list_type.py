a = ['a', 'b', 'c', 'd']
b = (1 ,2 ,3 ,4, 5)
list_set = {1, 2, 3, 4, 5, 6, 7, 7, 7, 1, 2, 3, 'a'}
#print(list_set)
my_first_dict = {
    'name' : 'Ivan',
    'age' : 25,
    'lol' : 'Yes',
    'City' : 'New',
    'Is new' : True
}

my_first_dict['age'] = 44
my_first_dict['LoL'] = True
#print(my_first_dict)
for key, value in my_first_dict.items():
    print(f'{value}')