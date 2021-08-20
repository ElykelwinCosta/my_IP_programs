def ehBissexto(ano):
  if ((ano%400==0) or (ano%4==0  and ano%100!=0)):
    return True
  else:
    return False

def ehDiaValido(dia, mes, ano):
  if (mes==4) or (mes==6) or (mes==9) or (mes==11):
    if (dia>=1 and dia<=30):
      return True
  elif (mes==1) or (mes==3) or (mes==5) or (mes==7) or (mes==8) or (mes==10) or (mes==12):
    if (dia>=1 and dia<=31):
      return True
  elif (mes==2):
    if (dia>=1 and dia<=28):
      return True
    elif (dia ==29 and ehBissexto(ano)):
      return True
  return False
  
#PROGRAMA PRINCIPAL
data = input().split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
x = ehDiaValido(dia,mes,ano)
if (x==True ):
    print("Data Válida")
else:
    print("Data inválida")
