from command import WappyCommand
from interface import WappyInterface

class WappyClient:
    def __init__(self, interface_webdriver, client_name):
        self.interface = WappyInterface(interface_webdriver, self)
        self.name = client_name
        self.commands = []

    def help(self, help_with=""):
        # This function is always available for chat users, and callable with '/help'
        if help_with == "":
            # Map out all loaded commands and their usage
            help_string = f"""
            *{self.name}*
            The following commands are available:
            """
            for cmd in self.commands:
                    help_string += f"➳ _{cmd.get_usage()}_ \n"
        else:
            for cmd in self.commands:
                if cmd.name == help_with:
                    help_string = cmd.get_usage()
            
        return help_string

    def initialize_commands(self, function_list):
        self.commands.append(WappyCommand(self.help))
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
        self.interface.run()

    def stop(self):
        print(f"Stopping Wappy Client named {self.name}")
        self.running = False
