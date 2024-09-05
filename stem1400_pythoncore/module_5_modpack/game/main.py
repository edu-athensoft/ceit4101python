"""
main
"""
import stem1400_pythoncore.module_5_modpack.game.level.load as levelload
import stem1400_pythoncore.module_5_modpack.game.level.over as levelover
import stem1400_pythoncore.module_5_modpack.game.level.start as levelstart

import stem1400_pythoncore.module_5_modpack.game.image.open as imgopen
import stem1400_pythoncore.module_5_modpack.game.sound.load as sndload

# main program of game
print("=== My Game Framework ===")

print("starting game...")
img = 'main.jpg'
imgopen.open(img)

music = "bgm.mp3"
sndload.load(music)
print()

# load level, image and music
print("loading level...")
level = 1
levelload.load(level)

# start gaming
print("\nstarting level...")
levelstart.start()
print()

# stop gaming
levelover.over()

print("=== Game Over ===")