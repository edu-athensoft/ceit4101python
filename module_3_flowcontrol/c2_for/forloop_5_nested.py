# print out a matrix

"""
out put like
11,12,13
21,22,23
31,32,33

(11,12,13)
(21,22,23)
(31,32,33)

matrix = ((11,12,13),(21,22,23),(31,32,33))

loop for each row
    round 0:    (11,12,13) -> row 0 -> matrix[0]
        Loop for each column
            round 0:    11  -> matrix[0][0]
            round 1:    12  -> matrix[0][1]
            round 2:    13  -> matrix[0][2]
    round 1:    (21,22,23) -> row 1 -> matrix[1]
        Loop for each column
            round 0:    21  -> matrix[1][0]
            round 1:    22  -> matrix[1][1]
            round 2:    23  -> matrix[1][2]
    round 2:    (31,32,33) -> row 2 -> matrix[2]
        Loop for each column
            round 0:    31  -> matrix[2][0]
            round 1:    32  -> matrix[2][1]
            round 2:    33  -> matrix[2][2]
"""

matrix = ((11,12,13),(21,22,23),(31,32,33))

for row in matrix:
    # print(row)
    for col in row:
        print(col, end="\t")
    print()





