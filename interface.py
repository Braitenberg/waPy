from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from message import WappyMessage

from time import sleep


class WappyInterface:
    # Interface between the wappy client and the webdriver/browser
    def __init__(self, webdriver_type, wappy_client):
        self.client = wappy_client
        self.webdriver_type = webdriver_type
        self.webdriver = None
        self.read_msg = None
        self.active = False
        self.check_interval = 1  # Non-customizable for now, may cause instability

    def start(self):
        print('Interface called, booting webdriver...')
        if self.webdriver_type.lower() == 'chrome':

            options = webdriver.ChromeOptions()
            options.add_argument('--user-data-dir=./User_Data')

            self.webdriver = webdriver.Chrome(chrome_options=options)
            self.webdriver.get("https://web.whatsapp.com/")

            print(
                f'driver {self.webdriver_type} booted! Awaiting whatsapp activation...')

            try:
                WebDriverWait(self.webdriver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@class="X7YrQ"]')))
            finally:
                print('Nessecary elements loaded! Listening for queries...')
                self.active = True
                while self.active:
                    self.execute_cmd_queries()
                    sleep(self.check_interval)

        else:
            raise ValueError(f"Invalid driver type: '{self.webdriver_type}'.")

    def stop(self):
        print(f"Stopping interface of client '{self.client.name}'")
        self.active = False
        self.webdriver.close()

    def execute_cmd_queries(self):
        last_msg = self.get_last_msg()
        if self.read_msg:
            if self.read_msg.web_element != last_msg.web_element and last_msg.is_query():
                result = self.execute(last_msg)
                if result:
                    self.post_text(result)

        self.read_msg = last_msg

    def get_last_msg(self):
        # Gets the web element of the last message received on the watsapp web client

        chat_pane = '//*[@class="X7YrQ"]'
        message = '//*[@class="FTBzM"]'

        driver = self.webdriver
        chat_panes = driver.find_elements_by_xpath(
            chat_pane)  # Represents all your chats
        for pane in chat_panes:
            if "transform: translateY(0px);" in pane.get_attribute("style"):
                last_active = pane
                last_active.click()

                WebDriverWait(self.webdriver, 2).until(
                    EC.presence_of_element_located((By.XPATH, message)))

                text_messages = driver.find_elements_by_xpath(message)

                print(len(text_messages))
                print("LAST MESSAGE FOUND: ", text_messages[-1])
                return WappyMessage(web_element=text_messages[-1])

    def execute(self, message):
        query_name = message.get_query_name()
        if query_name in self.client.commands:
            return self.client.commands.cmd_name.execute(message.get_kwargs())
        else:
            print(
                f"Query {query_name} not found in client named {self.client.name}.")
            return False

    def post_text(self, msg):
        # TODO: Post a message to the watsapp web client
        pass
