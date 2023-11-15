"""
package:    level
module:     over
"""

import archived.py200622_python2.day11_py200727.game.image.close as imgclose
import archived.py200622_python2.day11_py200727.game.sound.pause as sndpause


def over():
    print(f"level.over()")

    img = 'map.jpg'
    imgclose.close(img)

    img = 'char.png'
    imgclose.close(img)

    img = 'img1.png'
    imgclose.close(img)

    img = 'img2.png'
    imgclose.close(img)

    music = 'bgm.mp3'
    sndpause.pause(music)