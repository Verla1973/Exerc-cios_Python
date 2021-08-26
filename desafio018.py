import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print(f'O seno do ângulo {an} é {seno:.2f}')

coseno = math.cos(math.radians(an))
print(f'O coseno do ângulo {an} é {coseno:.2f}')

tangente = math.tan(math.radians(an))
print(f'A tangente do ângulo {an} é {tangente:.2f}')
