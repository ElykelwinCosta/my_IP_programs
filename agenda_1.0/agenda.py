#Faça um programa chamado "Agenda.py" que leia “n” nomes e “n” telefones e onde depois se possa pesquisar o telefone da pessoa a partir do seu nome ou então o nome da pessoa que tem um certo telefone.
#Dica 1: Cria uma lista para os nomes e uma lista para os telefones e leia ambas no mesmo laço
#Dica 2: Crie uma função pesquisaNomePeloTelefone(tel, listaNomes, listaTelefones)
#Dica 3: Crie uma função pesquisaTelefonePeloNome(nome, listaNomes, listaTelefones)

#FUNÇÕES
def pesquisaTelefonePeloNome(nome, listaNomes, listaTelefones):
    for k in range(len(listaNomes)):
        if (listaNomes[k] == nome):
            return listaTelefones[k]
    return "Contato não encontrado"
    

def  pesquisaNomePeloTelefone(tel, listaNomes, listaTelefones):
    for k in range(len(listaTelefones)):
        if (listaTelefones[k]==tel):
            return listaNomes[k]
    return "Telefone não encontrado"




#PROGRAMA PRINCIPAL
nomes = []
telefones = []


N = int(input("Digite a quantidade de contatos que deseja adicionar: "))

for k in range(N):
    nome = input("Digite o nome do contato {}: ".format(k+1))
    tel = input("Digite o telefone do contato {}: ".format(nome))
    nomes.append(nome)
    telefones.append(tel)

telefoneAPesquisar = input("Qual o número do contato que deseja pesquisar: ")
nome = pesquisaNomePeloTelefone(telefoneAPesquisar, nomes, telefones)
print("Contato: {} | Telefone: {}".format(nome, telefoneAPesquisar))


nomeAPesquisar = input("Qual o contato que você quer pesquisar?")
telefoneEncontrado = pesquisaTelefonePeloNome(nomeAPesquisar, nomes, telefones)
print("Contato: {} | Telefone: {}".format(nome, telefoneEncontrado))



