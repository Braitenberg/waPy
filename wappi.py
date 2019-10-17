from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

class WappiWebInterface:
    webDrivers = {
        "firefox": webdriver.Firefox,
        "chrome": webdriver.Chrome
    }

    def __init__(self, webDriver, parentClient):
        if self.webDrivers[webDriver]:
            self.webDriver = webDriver
        else:
            error_string = 'Could not find webdriver %s' % webDriver
            raise Exception(error_string)

        self.parentClient = parentClient

    def commandListener(self):
        # Listen for command
        driver = self.webDriver()
        driver.get("https://web.whatsapp.com/")

        text = 0
        return self.parentClient.execute(text)

class WappiClient:
    def __init__(self, webDriver, name):
        self.webInterface = WappiWebInterface(webDriver=webDriver, parentClient=self)
        self.collections = []
        self.name = name

    def execute(self, functionName, args=[]):
        for collection in self.collections:
            if collection.functionName:
                return collection.executeFunction(functionName, args)

    def addCollection(self, collection):
        return self.collections.append(collection)

class WappiCollection:
    def executeFunction(functionName, args=[]):
        print(f'executing function {functionName} with args {args}...')
        return functionName(args)
    pass

class CustomCollection(WappiCollection):
    def helloWorld(self, userName):
        return f"hello world, {userName}" 

collection = CustomCollection()
wappi = WappiClient('firefox', 'custom')
wappi.addCollection(collection)