"""
quiz 332

3. Please write a program to print out every item in the nested list as follows:
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Hint:  Using for-loop

"""

numbers = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j])
