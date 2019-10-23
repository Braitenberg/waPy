import logging

class WappyCommand:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__
        self.kwargs = function.__code__.co_varnames
        self.usage_string = ""

    def get_usage(self):
        if self.usage_string == "":
            # Generate usage string if not yet defined
            # Format: "/[command_name] <arg1>  <arg2>  <arg3> ... "
            new_usage_string = f"/{self.function.__name__}"
            for kwarg in self.kwargs:
                # Maps out the arguments of the given function
                new_usage_string += f" <{kwarg}>"
            self.usage_string = new_usage_string
        return self.usage_string

    def execute(self, *args, **kwargs):
        # Called when webdriver detects the command is queried by user
        logging.info(f"Executing command '{self.name}'")
        return self.function(*args, **kwargs)
