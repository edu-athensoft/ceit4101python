"""
demo 06.

char walking
clock tick

clock = pygame.time.Clock()
clock.tick(num)

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
game settings
"""
clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        # set char
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.offset = 5
        # set jump
        self.isJump = False
        self.jumpCount = 9
        self.JUMP_CNT = 9
        # set walk
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walk_left[self.walkCount % 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walk_right[self.walkCount % 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char_img, (self.x, self.y))


def redraw_win():
    win.blit(bg_img, (0,0))
    # win.blit(char_img, (0, 420))
    man.draw(win)
    pygame.display.update()


def redraw_char():
    win.blit(char_img, (0,420))
    pygame.display.update()


"""
main program
"""
man = player(300, 410, 64, 64)

run = True
while run:
    # frame rate FPS = 60
    # pygame.time.delay(17)
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # key settings for movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x >= man.offset:
        man.x -= man.offset
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x <= WIN_WIDTH-man.width-man.offset:
        man.x += man.offset
        man.left = False
        man.right = True
    else:
        man.left = False
        man.right = False
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -man.JUMP_CNT:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = man.JUMP_CNT

    # print(f"x={x},y={y}")
    redraw_win()
    # redraw_char()

"""
finalize
"""
pygame.quit()






