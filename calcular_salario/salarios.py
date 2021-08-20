listaSalarios = []
nomesFuncionarios = []
totalSalarios = 0.0

quantidadeFuncionarios = int(input("Quantos funcionários há na empresa? "))

for k in range(quantidadeFuncionarios):
  nomeFuncionario = input("Qual o nome do funcionário? ")
  nomesFuncionarios.append(nomeFuncionario)
  numHoras = int(input("Quantas horas ele trabalhou? "))
  valorPorHora = float(input("Qual o valor da hora de trabalho dele? "))
  valorRecebido = (numHoras*valorPorHora)
  listaSalarios.append(valorRecebido)
  print("O salário do funcionário %s é: R$ %.2f\n" %(nomeFuncionario, valorRecebido))
  totalSalarios += valorRecebido

print("O total gasto com salários foi R$ %.2f\n" %totalSalarios)

#Descobrir maior salario
maiorSalario = 0.0
nomeFuncionarioRico = ""
for k in range(quantidadeFuncionarios):
    if (listaSalarios[k]>=maiorSalario):
        maiorSalario= listaSalarios[k]
        nomeFuncionarioRico = nomesFuncionarios[k]

print("O funcionário que recebeu maior salário foi %s" %nomeFuncionarioRico)





        
