
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Fim da contagem!")
number = int(input("Digite um número para iniciar a contagem regressiva: "))    
countdown(number)