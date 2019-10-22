class WappyMessage:
    def __init__(self, web_element):
        self.web_element = web_element

    def is_query(self):
        return str.startswith(self.get_text, "/")

    def get_text(self):
        # TODO: get text from web_element
        return "TODO: MSG-TEXT"

    def get_query_name(self, query):
        # TODO: select the first word in the web_element
        return "TODO: CMDNAME"

    def get_kwargs(self):
        # TODO: Return kwargs found in query
        return "TODO: KWARGS"
