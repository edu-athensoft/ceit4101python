str_list = ['a','b','c','d']

num_list = list(range(4))


for n in num_list:
    for s in str_list:
        print(s, end='\t')
    print()