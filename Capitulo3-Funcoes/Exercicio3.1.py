'''
Escreva uma função chamada right_justify, que receba uma string chamada s como 
parametro e exiba a string com espaços sufucientes à frente para que a ùltima letra
da string string esteja na coluna 70 da tela :

right_justify('monty')

Dica: use concatenação  de strings e repetições. Além disso, o Python oferece uma 
função integrada chamada len, que representa o comprimento de uma string, então o 
valor de len('monty') é 5


'''

def right_justify(s):
    #Calculo de espaços para que a ultima letra esteja na coluna 70
    num_espaco = 70 - len(s)
    
    #concatenando a string com os números de espaços 
    jus_str = " " * num_espaco + s

    #exibindo a string
    print (jus_str)

right_justify("monty")