import funcoes

#PROGRAMA PRINCIPAL
n1 = float(input("Digite a nota 1"))
n2 = float(input("Digite a nota 2"))
n3 = float(input("Digite a nota 3"))
print("A média é:")
print(funcoes.mediaAritmetica2(n1,n2,n3))
lista = [n1,n2,n3]
print(funcoes.mediaAritmetica(lista))
