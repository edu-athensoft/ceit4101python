"""
demo 06.

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
WIN_WIDTH = 852
WIN_HEIGHT = 480
win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# refill with background color
win.fill((255,255,255))

# set caption of windows
pygame.display.set_caption("Athensoft Python Game Demo")

"""
sprite
"""
bg_img = pygame.image.load('pics/'+'bg.jpg')
char_img = pygame.image.load('pics/'+'standing.png')
walk_left_imgs = ['L1.png','L2.png','L3.png','L4.png','L5.png','L6.png']
walk_right_imgs = ['R1.png','R2.png','R3.png','R4.png','R5.png','R6.png']
walk_left = []
walk_right = []

for img in walk_left_imgs:
    walk_left.append(pygame.image.load('pics/'+img))

for img in walk_right_imgs:
    walk_right.append(pygame.image.load('pics/'+img))

# test
print(walk_left)
print(walk_right)


"""
set objects
"""
# original coord
x, y = 50, 420

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
JUMP_CNT = 10
jumpCount = JUMP_CNT


"""
set walk
"""
walkCount = 0
left = False
right = True


def redraw_win():
    global walkCount

    # print(f"walkCount={walkCount}")

    win.blit(bg_img, (0,0))
    # win.blit(char_img, (0, 420))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walk_left[walkCount % 3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walk_right[walkCount % 3], (x,y))
        walkCount += 1
    else:
        win.blit(char_img, (x,y))

    pygame.display.update()


def redraw_char():
    win.blit(char_img, (0,420))
    pygame.display.update()


"""
main program
"""
run = True
while run:
    # frame rate FPS = 60
    pygame.time.delay(17)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # key settings for movement
    keys = pygame.key.get_pressed()
    # print(keys,type(keys))

    if keys[pygame.K_LEFT] and x >= offset:
        x -= offset
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x <= WIN_WIDTH-width-offset:
        x += offset
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
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
    redraw_win()
    # redraw_char()

    # set current x and y
    myobject[0] = x
    myobject[1] = y




"""
finalize
"""
pygame.quit()






