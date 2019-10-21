# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import time
import sys

class WappyCommand:
    def __init__(self, function, kwargs):
        self.function = function
        self.kwargs = kwargs

    def get_usage(self):
        usage = f"/{self.function.__name__}" 
        # todo: for each argument, add it to the usage string as <arg>
        return usage

    def execute(self):
        return self.function(self.kwargs)


class WappyClient:
    def __init__(self, webDriver, name):
        # todo: add webdriver
        self.name = name
        self.commands = []

    def command(self, function):
        def init_command(**kwargs):
            newCmd = WappyCommand(function, kwargs)
            self.commands.append(newCmd)
            print(f"Initialized command {newCmd.get_usage()}")
        return init_command