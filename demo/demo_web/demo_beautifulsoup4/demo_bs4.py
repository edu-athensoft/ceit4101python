"""
beautiful soup 4
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>some<b>bad</b><i>HTML</i></p>")

print(soup.prettify())