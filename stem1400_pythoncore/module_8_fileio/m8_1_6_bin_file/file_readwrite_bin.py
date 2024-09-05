"""
read and write a binary file

image, base 64
index.html
https://www.coder.work/article/2435056
<img src="data:image/jpg;base64,place base64 code here"/>

"""

import base64

with open('pic1.jpg', 'rb') as f:
    image_data = f.read()
    base64_data = base64.b64encode(image_data)    # using base64
    print(base64_data)


