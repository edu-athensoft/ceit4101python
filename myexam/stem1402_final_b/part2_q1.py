"""
Exam No.:       STEM1402_FINAL_B
Course No.:     STEM1402
Course Name:    Python II-1

Problem:        Calculating TF
"""

"""
Solution:

1. create a dataset and separate it from programs
- creating dataset.py
- make it as a constant
- import it to the program
- test it

2. analyzing raw data
- identify stop words
- identify unnecessary numbers
- identify punctuations and symbols

notes:
- hyphen '-' is retained


3. load data

4. data clean
- pre-process data
- lower case
- remove stop words
- remove numbers
- remove punctuations and symbols

notes:
- must in order

5. TF

6. output
"""

import myexam.stem1402_final_b.dataset as dataset


def listwords(wordlist):
    """
    list all items of word in the given list
    :param wordlist:
    :return:
    """
    for word in wordlist:
        print(f"|{word}|")


def remove_content(mylist, target):
    """
    remove all target contents from the given list
    :param mylist: original list which may contain the target
    :param target: item to be removed
    :return:
    """
    for i in range(len(mylist)):
        if target in mylist:
            mylist.remove(target)
    return mylist


# set list of strings to be removed
punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
stopwords= ['the', 'a', 'an', 'am','is', 'are', 'was', 'were', 'been','being','be','have','has','had',
            'of','for','from','to', 'in', 'on','at','upon','with','without','and','or','not',
            'by','as','before','after','during','over','between','beyond',
            'i','me','you','he','him', 'she','her','they','them','it',
            'my','your','his','their','mine','yours','hers','theirs',
            'much','more','such','many','more','most','all',
            'what','which','where','whose','how','whereas','when','however',
            'can','could','would','should','will','may','maybe','might',
            'that','this','those','these','there',
            'e.g.','e.g','eg','i.e.','i.e','ie']
numbers = []




# 3. load data
article = dataset.myarticle
# print(article)

# 4. data clean
# 4.1 pre-process data
raw_words = article.split()
print("=== raw words===")
# listwords(raw_words)
print(f"The word counts is: {len(raw_words)}")
print()


# 4.2 lower case
lowered_words = [word.lower() for word in raw_words]
print("=== lowered words===")
# listwords(raw_words)
print(f"The word counts is: {len(raw_words)}")
print()

# 4.3 remove content
# 4.3.1 remove punctuations and symbols, numbers
list_without_punc = lowered_words
for i in range(len(list_without_punc)):
    for char in list_without_punc[i]:
        if char in punctuations:
            list_without_punc[i] = list_without_punc[i].replace(char, '')
        if char.isdigit():
            list_without_punc[i] = list_without_punc[i].replace(char, '')
print("=== removing punctuations and symbols ===")
# listwords(list_without_punc)
print(f"The word counts is: {len(list_without_punc)}")
print()

# 4.3.2 remove stop words
list_without_stopword = list_without_punc.copy()
for i in range(len(list_without_punc)):
    if list_without_punc[i] in stopwords:
        list_without_stopword.remove(list_without_punc[i])
print("=== removing stop words ===")
print(f"The word counts is: {len(list_without_stopword)}")
# listwords(list_without_stopword)
print()

# 5. TF
# TF = count of target word / count of total words
total_words = list_without_stopword
count_total = len(total_words)
total_word_set = set(total_words)
print("=== identifying unique words ===")
print(f"The word counts is: {len(total_word_set)}")
print()

# occurrences and tf
result_tf= []
for unique_word in total_word_set:
    count = total_words.count(unique_word)
    tf = count / count_total
    result_tf.append((count, tf, unique_word))
    # print(f"{count:<3} times of {unique_word}")

print("=== occurrences and TF of each word ===")
print(result_tf)
print()

# sorting
result_tf.sort(reverse=True)
print("=== sorted occurrences and TF of each word ===")
print(result_tf)
print()

# 6. Output result
print("=== The most frequent words in the article ===")
count_show = 0
MAX_ITEM = 8
for item in result_tf:
    if count_show <= MAX_ITEM:
        print(f"{item[0]:3} times {item[1]:8.4f} {item[1]:8.2%} {item[2]}")
    else:
        break
    count_show += 1











