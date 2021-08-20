def mediaAritmetica2(nota1, nota2, nota3):
    return (nota1+nota2+nota3)/3


def mediaAritmetica(notas):
    soma = 0.0
    for nota in notas:
        soma+=nota
    if (len(notas)==0):
        return 0.0
    else:
        media = soma/len(notas)
        return media
    









      
