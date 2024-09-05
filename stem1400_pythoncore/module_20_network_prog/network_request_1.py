"""
requests
https, http
"""

import requests


def fetch_homepage(url):
    # send GET request
    response = requests.get(url)

    # return content in response
    return response.text


# read web content of homepage
url = "https://www.athensoft.com"
homepage_content = fetch_homepage(url)
print(homepage_content)
