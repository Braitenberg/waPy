from command import WappyCommand
from interface import WappyInterface

class WappyClient:
    def __init__(self, interface_webdriver, client_name):
        self.interface = WappyInterface(interface_webdriver, self)
        self.name = client_name
        self.commands = []

    def initialize_commands(self, function_list):
        if type(function_list) is list:
            for function in function_list:
                newCmd = WappyCommand(function)
                self.commands.append(newCmd)
                print(f"Initialized command '{newCmd.get_usage()}'")
        else:
            raise ValueError(
                f"Invalid argument for 'function_list'. Expected list, but {type(function_list)} was passed")

    def run(self):
        print(f"Starting Wappy Client named {self.name}")
        self.interface.start()

    def stop(self):
        print(f"Stopping Wappy Client named {self.name}")
        self.running = False
