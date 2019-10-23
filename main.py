from client import WappyClient

wappy = WappyClient(interface_webdriver='chrome', client_name='tritri-bot')


def helloworld(name):
    print('CALLED')
    return f'Hello, {name}'


def getmoney(iban_number, valuta):
    return f"Yes, {iban_number} is a millionaire in {valuta}'s."


wappy.initialize_commands([helloworld, getmoney])
wappy.run()
