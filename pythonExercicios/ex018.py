# Digite o ângulo e o programa retorna os valores do SENO, COSSENO e TANGENTE em radianos.

import math
angulo = int(input('Digite o ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno de {}° é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))