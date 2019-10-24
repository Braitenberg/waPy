import re
import logging


class WappyMessage:
    def __init__(self, web_element):
        self.web_element = web_element
        self.text = False

    def is_query(self):
        return str.startswith(self.get_text(), "/")

    def get_text(self):
        # TODO: make text_field.text work with emojis
        text = ""
        if self.text:
            return self.text

        try:
            text_field = self.web_element.find_element_by_class_name(
                "selectable-text")
            text = text_field.text
        except:
            # TODO: Specify to selenium.noSuchElementException
            text = "NOT-TEXT"
        return text

    def get_query_name(self):
        text = self.get_text() + ' '
        found = re.findall("/(\\w+) ", text)
        name = ""
        if found != []:
            name = found[0]
            
        return name

    def get_sender(self):
        # TODO: Get sender of this message
        return ""

    def get_args(self):
        found = re.findall("/\\w+ (.*)", self.get_text())
        if len(found) >= 1:
            args = found[0].split(' ')
        else:
            args = []
        return args
