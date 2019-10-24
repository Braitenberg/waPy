from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command

from waPy.message import WappyMessage

from time import sleep
import logging

class WappyInterface:
    # Interface between the wappy client and the webdriver/browser
    def __init__(self, webdriver_type, wappy_client):
        self.client = wappy_client
        self.webdriver_type = webdriver_type
        self.webdriver = None
        self.read_msg = None
        self.active = False
        self.done = None
        self.check_interval = 1  # Non-customizable for now, may cause instability

    def run(self):
        logging.info("Interface called, booting webdriver...")
        self.webdriver = self.create_driver(self.webdriver_type)
        self.webdriver.get("https://web.whatsapp.com/") 
        logging.info(
            f"{self.webdriver_type} driver booted! Awaiting whatsapp activation...")

        try:
            WebDriverWait(self.webdriver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="X7YrQ"]')))
        except:
            self.stop()

        logging.info('Necessary elements loaded! Listening for queries...')
        self.active = True

        while self.active:
            self.execute_cmd_queries()
            sleep(self.check_interval)

    def stop(self):
        logging.info(f"Stopping interface of client '{self.client.name}'")
        self.active = False
        self.webdriver.close()

    def create_driver(self, type):
        if type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--user-data-dir=./User_Data')
            return webdriver.Chrome(chrome_options=options)
        else:
            raise ValueError(f"Invalid driver type: '{self.webdriver_type}'.")

    def execute_cmd_queries(self):
        last_msg = self.get_last_msg()
        if self.done:
            if last_msg.get_text() != self.done.get_text():
                if last_msg.is_query():
                    self.post_text(self.execute_cmd(last_msg)) 

        elif last_msg.is_query():
            self.post_text(self.execute_cmd(last_msg)) 

        self.done = last_msg

    

    def execute_cmd(self, message):
        query_name = message.get_query_name()
        sender = message.get_sender()

        logging.info(f"User '{sender}' queried '{query_name}'.")
        result = f"Query '{query_name}' not found in client '{self.client.name}'."
        for cmd in self.client.commands:
            if cmd.name == query_name:
                try:
                    result = cmd.execute(*message.get_args())
                except Exception as exception:
                    result = f"_{str(exception)}_ \n For more information, type '/help {query_name}'"
        
        return result

    def get_last_msg(self):
        # Gets the web element of the last message received on the watsapp web client
        chat_pane = '//*[@class="X7YrQ"]'
        message = '//*[contains(@class, "FTBzM")]'

        chat_panes = self.webdriver.find_elements_by_xpath(
            chat_pane)  # Represents all your chats

        attempts = 0
        while attempts <= 3:
            try:
                self.get_last_active(chat_panes).click()
            except Exception as error:
                logging.warning(f"While clicking active pane, an error occured: {error}") 
                if attempts == 3:
                    logging.error("Attempt limit reached, closing interface...")
                    self.stop()
                else:
                    logging.info("Retrying click...")
                    sleep(self.check_interval)
                    continue

            attempts += 1
            


        WebDriverWait(self.webdriver, 5).until(
            EC.presence_of_element_located((By.XPATH, message)))

        text_messages = self.webdriver.find_elements_by_xpath(message)

        return WappyMessage(web_element=text_messages[-1])

    def get_last_active(self, panes):
        # Loops through chat panes (left of the screen) and selects the top one
         for pane in panes:
            if "transform: translateY(0px);" in pane.get_attribute("style"):
                return pane

    def post_text(self, msg):
        # Simulates keyboard input to the browser and sends a message
        post_field = self.webdriver.find_element_by_class_name("_3u328")
        post_field.send_keys(msg)
        post_field.send_keys(Keys.RETURN)
