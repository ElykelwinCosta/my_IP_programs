import random

num = random.randint(1,100)
acertou = False
pontos = 100
while( acertou == False):
    
    x = int(input("Digite um número [1-100]"))

    if (x == num):
        print("Parabéns! Você acertou!. Pontos: ",pontos)
        acertou = True
        
    elif (num>x):
        print("Errou. O número procurado é maior! ")
        pontos -= 1
        
    else:
        print("Errou. O número procurado é menor! ")
        pontos -= 1


print("Fim do programa")


