"""
package:    level
module:     over
"""

import stem1400_modules.module_5_modpack.game.image.close as imgclose
import stem1400_modules.module_5_modpack.game.sound.pause as sndpause


def over():
    print("exiting current game level...")
    print(f"level.over()")

    img = 'map.jpg'
    imgclose.close(img)

    img = 'char.png'
    imgclose.close(img)

    img = 'img1.png'
    imgclose.close(img)

    img = 'img2.png'
    imgclose.close(img)

    print("\nexiting game...")

    music = 'bgm.mp3'
    sndpause.pause(music)

    img = 'main.jpg'
    imgclose.close(img)