"""
package:    level
module:     start
"""

import stem1400_pythoncore.module_5_modpack.game.image.open as imgopen

def start():
    print(f"level.start()")

    img = 'map.jpg'
    imgopen.open(img)

    img = 'char.png'
    imgopen.open(img)

    img = 'img1.png'
    imgopen.open(img)

    img = 'img2.png'
    imgopen.open(img)

    # play game
    print("playing game...")

