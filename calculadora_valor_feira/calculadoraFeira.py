print("CALCULADORA DA FEIRA")

nomeProduto = input("Qual produto você quer comprar? ");
quantProdutos = int(input("Quantas unidades do produto você vai querer? "))
preco = float(input("Qual o preço de cada unidade do produto? "))
subtotal = preco*quantProdutos

print("Sub-total para este produto: ",subtotal)
desconto = float(input("Qual o desconto percentual que você recebeu? "))
valorComDesconto = subtotal -((desconto*subtotal)/100)
print("Você vai pagar %.2f pelo produto %s" %(valorComDesconto,nomeProduto))

