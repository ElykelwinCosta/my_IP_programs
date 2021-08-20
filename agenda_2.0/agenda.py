def leContatosDeArquivo(nomeArquivo):
  arquivo = open(nomeArquivo, 'r')
  linhas = []
  for linha in arquivo:
      linhaLida = linha.strip().split("#")
      linhas.append(linhaLida)
  arquivo.close()
  return linhas

def gravaContatosEmArquivo(contatos, nomeArquivo):
  arquivo = open(nomeArquivo,'w')
  for nome, telefone, bairro, dia, mes in contatos:
      linha = nome + "#" + telefone + "#" + bairro + "#" + dia + "#"+ mes + "\n"
      arquivo.write(linha)
  arquivo.close()

def listaContatos(contatos):
  if (len(contatos) == 0):
    print("A agenda está vazia!")
    
  else:
    for linha in contatos:
      print("Nome:",linha[0],", Telefone:", linha[1], ", Bairro:", linha[2], ", Aniversário:",linha[3],"/",linha[4])


def listaContatosIniciadosCom(letra, contatos):
    print("CONTATOS COM PREFIXO:",letra)
    for nome, telefone, bairro, dia, mes in contatos:
        if (nome.upper()[0]== letra.upper()):
            print("Nome:", nome, ", Telefone:", telefone, ", Bairro:", bairro, ", Aniversário:", dia,"/",mes)
          
def pesquisaAniversarioDe(nomePesq, contatos):
  for nome, telefone, bairro, dia, mes in contatos:
    if (nomePesq==nome):
      print(dia,"/",mes)

  
#PROGRAMA PRINCIPAL
  
contatos = leContatosDeArquivo("AgendaRioTinto.txt")
if(len(contatos) > 0):
  numLinhas = len(contatos)
  numColunas = len(contatos[0])
  print("Número de contatos lidos:",numLinhas)
  print("Número de dados de cada contato:", numColunas)

else:
  print("Número de contatos lidos: 0")

sair = False
while(sair == False):
    opcao = int(input("\n1.Listar contatos\n" +
                      "2.Pesquisar aniversario pelo nome\n" +
                      "3.Pesquisar contatos do bairro\n" +
                      "4.Pesquisar aniversariantes do mês\n" +
                      "5.Cadastrar Contato\n" +
                      "6.Salvar dados\n" +
                      "7.Listar contatos com letra...\n" +
                      "8.Sair\n\n" +
                      "Digite uma opção: "))

    if (opcao == 1):
        listaContatos(contatos)

    elif (opcao == 2):
        nomePesq = input("Qual o nome a pesquisar?")
        pesquisaAniversarioDe(nomePesq, contatos)

    elif (opcao == 5):
        nome = input("Digite o nome da pessoa: ")
        telefone = input("Digite o telefone: ")
        bairro = input("Digite o bairro em que mora: ")
        diaAniversario = input("Digite o dia do aniversário: ")
        mesAniversario = input("Digite o mês do aniversário: ")
        contato = [nome, telefone, bairro, diaAniversario, mesAniversario]
        contatos.append(contato)

    elif (opcao ==6):
        gravaContatosEmArquivo(contatos, "AgendaRioTinto.txt")

    elif (opcao == 7):
        letra = input("Qual a letra a pesquisar?")
        listaContatosIniciadosCom(letra, contatos)

    elif (opcao ==8):
        sair = True

print("FIM DO PROGRAMA. ATÉ MAIS")
