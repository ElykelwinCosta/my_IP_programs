print("CALCULADORA DE GASTOS")
gastoAlimentacao = 0
gastoTransporte = 0
gastoLazer = 0
outrosGastos= 0
n = int(input("Quantos gastos você teve essa semana? "))
for gasto in range(n):
  valorGasto = float(input("\nQual o valor gasto? "))
  tipoGasto = int(input("Qual tipo de gasto? 1.Alimentação. 2.Transporte 3. Lazer 4.Outros "))
  if (tipoGasto == 1):
    gastoAlimentacao= gastoAlimentacao + valorGasto
  elif (tipoGasto == 2):
    gastoTransporte += valorGasto
  elif (tipoGasto == 3):
    gastoLazer+= valorGasto
  else:
    outrosGastos+= valorGasto


print("Você gastou R$ %.2f com alimentação" %gastoAlimentacao)
print("Você gastou R$ %.2f com transporte" %gastoTransporte)
print("Você gastou R$ %.2f com lazer" %gastoLazer)
print("Você gastou R$ %.2f com outros gastos\n" %outrosGastos)
total = gastoAlimentacao+gastoTransporte+gastoLazer+outrosGastos
print("Total gasto: R$ %.2f\n" %total)

gastoPercentualAlimentacao = (gastoAlimentacao/total)*100
gastoPercentualTransporte = (gastoTransporte/total)*100
gastoPercentualLazer = (gastoLazer/total)*100
gastoPercentualOutros = (outrosGastos/total)*100

print("%.2f %% dos gastos foram com alimentação" %gastoPercentualAlimentacao)
print("%.2f %% dos gastos foram com transporte" %gastoPercentualTransporte)
print("%.2f %% dos gastos foram com lazer" %gastoPercentualLazer)
print("%.2f %% dos gastos foram com outros gastos" %gastoPercentualOutros)

