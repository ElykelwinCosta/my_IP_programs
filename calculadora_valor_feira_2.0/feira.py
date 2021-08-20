print("CALCULADORA DA FEIRA")

n = int(input("Quantos produtos você quer ler? "))
total = 0.0

for k in range(n):
   nomeProduto = input("Qual produto você quer comprar? ");
   quantProdutos = int(input("Quantas unidades do produto você vai querer? "))
   preco = float(input("Qual o preço de cada unidade do produto? "))
   subtotal = preco*quantProdutos
   print("Subtotal para este produto: R$ {:.2f}\n".format(subtotal))
   total += subtotal


print("O subtotal de suas compras é: R$ {:.2f}\n".format(total))   
desconto = float(input("Qual o desconto percentual que você recebeu? (somente números) "))
valorComDesconto = total -((desconto*total)/100)
print("O valor total de suas compras é: R$ {:.2f}".format(valorComDesconto))
