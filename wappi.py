from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

class WappiClient:
    def __init__(self, webDriver, name):
        # todo: add webdriver
        self.name = name

    def action(func):
        # https://realpython.com/primer-on-python-decorators/
        return 0


wappi = WappiClient(webDriver='firefox', name='john')

@wappi.action
def hello_world(name):
    print(f'Hello, {name}!')

hello_world('tristan')



