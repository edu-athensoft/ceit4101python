# string method

a = ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
print(a, type(a))
print()

# string.join()
result = ' '.join(a)
print(result, type(result))

result = ''.join(a)
print(result, type(result))

result = ','.join(a)
print(result, type(result))
print()