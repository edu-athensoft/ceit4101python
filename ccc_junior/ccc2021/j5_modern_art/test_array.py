"""
test array
"""
R = 2
C = 3
# canvas =[['B']*C]*R
canvas =[['B', 'B', 'B'], ['B', 'B', 'B']]
print(canvas)

def printCanvas(canvas):
    for rows in canvas:
        for col in rows:
            print(col,end='')
        print()

# printCanvas(canvas)

canvas[1][2] = 'G'
printCanvas(canvas)
