"""
main
"""
import archived.py200622_python2.day11_py200727.game.level.load as levelload
import archived.py200622_python2.day11_py200727.game.level.over as levelover
import archived.py200622_python2.day11_py200727.game.level.start as levelstart

import archived.py200622_python2.day11_py200727.game.image.open as imgopen

import archived.py200622_python2.day11_py200727.game.sound.load as sndload

# main program of game
print("=== My Game Framework ===")

# load level, image and music
level = 1
levelload.load(level)

img = 'map.jpg'
imgopen.open(img)

music = "bgm.mp3"
sndload.load(music)
print()

# start gaming
levelstart.start()
print()

# stop gaming
levelover.over()

print("=== Game Over ===")