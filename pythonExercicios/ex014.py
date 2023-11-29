# Converter temperatura de °C para °F.

temperaturaC = int(input('Digite a temperatura em °C para convertê-la em °F. \n'))
temperaturaF = temperaturaC * 9 / 5 + 32

print('A temperatura de {}°C corresponde à {}°F'.format(temperaturaC, temperaturaF))