# Create a dictionary from a sequence of keys
# vowels keys
keys_set = {'a', 'e', 'i', 'o', 'u'}
vowels = dict.fromkeys(keys_set)
print(vowels)

keys_list = ['a', 'e', 'i', 'o', 'u']
vowels = dict.fromkeys(keys_list)
print(vowels)

keys_tuple = ['a', 'e', 'i', 'o', 'u']
vowels = dict.fromkeys(keys_tuple)
print(vowels)

keys_string = 'Hello'
vowels = dict.fromkeys(keys_string)
print(vowels)

print()


# Create a dictionary from a sequence of keys with value
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)
print()
print()


# Create a dictionary from mutable object list
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append(2)
print(vowels)