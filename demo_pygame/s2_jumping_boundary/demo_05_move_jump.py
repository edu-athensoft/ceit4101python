"""
demo 05.

jumping action
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
WIN_WIDTH = 800
WIN_HEIGHT = 600
win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# refill with background color
win.fill((255,255,255))

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
object_color = (128,0,128)

"""
set jump
"""
isJump = False
JUMP_CNT = 11
jumpCount = JUMP_CNT


"""
main program
"""
run = True
while run:
    # frame rate FPS = 60
    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # key settings for movement
    keys = pygame.key.get_pressed()
    # print(keys,type(keys))

    if keys[pygame.K_LEFT] and x >= offset:
        x -= offset

    if keys[pygame.K_RIGHT] and x <= WIN_WIDTH-width-offset:
        x += offset

    if not(isJump):
        if keys[pygame.K_UP] and y >= offset:
            y -= offset

        if keys[pygame.K_DOWN] and y <= WIN_HEIGHT-height-offset:
            y += offset

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -JUMP_CNT:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = JUMP_CNT

    # print(f"x={x},y={y}")

    # refill with background color
    win.fill((255,255,255))

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






