"""
module requests

https://pypi.org/project/requests/
"""

import requests

r = requests.get("https://api.github.com/repos/psf/requests")

print(r.json()['description'])


r = requests.get("https://athensoft.com/")

print(r.text)

