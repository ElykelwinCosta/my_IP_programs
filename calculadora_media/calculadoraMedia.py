
somaNotas = 0

for k in range(3):
    nota = int(input("Digite sua {}º nota: ".format(k+1)))

    if nota >= 7 :
        print("Ótima nota, continue assim!\n")
    else:
        print("Sua nota precisa melhorar, estude mais da próxima vez!\n")

    somaNotas += nota

media = somaNotas / 3

print("Sua média geral é: {:.2f}".format(media))

if (media < 7):
    print("Que pena, você foi reprovado")
else:
    print("Parabéns, você foi aprovado!")
