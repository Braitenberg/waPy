from waPy.client import WappyClient as client

wappy = client(client_name='example-bot')  # Create a client

# Define some custom-made functions....
def helloworld(name):
    return f"Hello, {name}"


def getmoney(name, valuta):
    return f"Yes, {name} is a millionaire in {valuta}'s."

 
# Add these functions to the client as commands
wappy.initialize_commands([helloworld, getmoney])

wappy.run()  # Open the browser, open whatsapp and listen for commands
