# waPy 
waPy is a module that interfaces Python functions to Whatsapp.

## Why waPy? ##
1. Because not being able to automate a chat application is sóóóóó 2010. 
2. Having a chat-api opens up many [possibities](https://top.gg/list/top).

The only automation possibilities Whatsapp has are for [businesses (?)](https://www.whatsapp.com/business/),
and they are quite limited.

## Getting Started ##
waPy uses [Selenium](https://github.com/SeleniumHQ/selenium) for browser automation.
You'll also need to install a webdriver, which can be controlled by selenium.

### Webdriver ###
Right now, the only available webdriver is the Chrome webdriver. 
This is because it allows session data to be saved in such a way that the user does not constantly have to re-activate their
Watsapp web, which is quite a hassle.

#### To install the chrome webdriver, follow these steps: ####
1. Downloaded the webdriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
2. Add the webdriver to your Path-variable like [so](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).

### Example ###
```python
from waPy import client

wappy = client(client_name='example-bot')  # Create a client

# Define some custom-made functions....
def helloworld(name):
    return f"Hello, {name}"


def getmoney(name, valuta):
    return f"Yes, {name} is a millionaire in {valuta}'s."


# Add these functions to the client as commands
wappy.initialize_commands([helloworld, getmoney])

wappy.run()  # Open the browser, open whatsapp and listen for commands
```

In whatsapp, when somebody sends `/helloworld Karen`, the client will reply with `Hello, Karen`.
