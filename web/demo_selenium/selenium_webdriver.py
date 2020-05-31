"""
selenium
Python language bindings for Selenium WebDriver.

The selenium package is used to automate web browser interaction from Python.

用from selenium import webdriver


driver = webdriver.Firefox()   # Firefox
# driver = webdriver.Firefox("驱动路径")

driver = webdriver.Chrome()    # Chrome

driver = webdriver.Ie()        # Internet Explorer

driver = webdriver.Edge()      # Edge浏览器

driver = webdriver.Opera()     # Opera浏览器

driver = webdriver.PhantomJS()   # PhantomJS

"""

from selenium import webdriver

br = webdriver.Chrome("D:\dev\selenium\webdriver\chromedriver.exe")

br.get("https://www.athensoft.com")

print("set dimension ")
br.set_window_size(800, 600)

input("Press any key to quit.")
br.quit()