from wappyClient import WappyClient

wappy = WappyClient(webDriver='firefox', name='john')

@wappy.command
def hello_world(name):
    print(f'Hello, {name}')

print(wappy.commands)
