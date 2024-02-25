'''
O valor de uma espera com raio r é (4/3)*pi * r*3, qual o volume de uma esfera com raio de 5 ?
'''
pi = 3.14 # aproximando pi para 3.14
r  = 5    # raio do exercicio
e  = 3    # valor que vou elevar 

volume_r = (4/3)*pi*(r**3) 

print (f"o volume de uma esfera com raio de 5 é: {round (volume_r, 3)}, arrendondando para a terceira casa e assumindo pi = {pi}")
