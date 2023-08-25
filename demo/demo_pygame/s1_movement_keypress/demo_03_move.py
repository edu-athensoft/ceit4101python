"""
demo 03.

moving objects by key press
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
width,height = 50,50

# step for moving
offset = 5

myobject = [x,y,width,height]
object_color = (255,255,0)


"""
main program
"""
run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # key settings for movement
    keys = pygame.key.get_pressed()
    # print(keys,type(keys))

    if keys[pygame.K_LEFT]:
        x -= offset

    if keys[pygame.K_RIGHT]:
        x += offset

    if keys[pygame.K_UP]:
        y -= offset

    if keys[pygame.K_DOWN]:
        y += offset

    print(f"x={x},y={y}")

    # refill with background color
    win.fill((0,0,0))

    # set current x and y
    myobject[0] = x
    myobject[1] = y

    # draw object
    pygame.draw.rect(win, object_color, myobject)

    # display update
    pygame.display.update()


"""
finalize
"""
pygame.quit()






