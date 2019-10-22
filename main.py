from client import WappyClient

wappy = WappyClient(interface_webdriver='firefox', client_name='tritri-bot')


def hello_world(name):
    return f'Hello, {name}'


def get_money(iban_number, valuta):
    return f"Yes, {iban_number} is a millionaire in {valuta}'s."


wappy.initialize_commands([hello_world, get_money])
wappy.run()
print('doing stuff...')
