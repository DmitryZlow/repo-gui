my_int = 10
my_float = 10.2
my_str = "Hello, bro"
my_list = ['B', '25']
my_tuple = ('C', '5')
my_dict = {'city': 'Moscow', 'country': 'Russia'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')


