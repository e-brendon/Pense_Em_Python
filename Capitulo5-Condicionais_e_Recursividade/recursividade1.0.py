# se n for 0 a função exibe Blastoff, senão ela subtrai 1 e chama a função novamente
def countdown (n):
    if n <= 0:
        print ('Blastoff!')
    else:
        print(n)
        countdown(n-1)
countdown(5)