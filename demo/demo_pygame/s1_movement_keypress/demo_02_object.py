"""
demo 02.

creating objects and display
"""

import pygame

"""
initialize
"""
pygame.init()


"""
display settings
"""
# create viewport/windows
win = pygame.display.set_mode((800,600))

# set caption of windows
pygame.display.set_caption("Athensoft Python Game Demo")


"""
set objects
"""
# original coord
x, y = 50, 50

# dimension
width,height = 40,60

# step for moving
offset = 5

myobject = (x,y,width,height)
object_color = (255,0,0)


"""
main program
"""
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(win, object_color, myobject)
    pygame.display.update()


"""
finalize
"""
pygame.quit()






