def cadastrarUsuario(listaUsuarios):
    dados = input("Digite os dados do usuário no formato: nome,cpf,email \n")
    usuario = dados.split(",")
    listaUsuarios.append(usuario)
    print('Usuário cadastrado com sucesso!')

def listarUsuarios(listaUsuarios):
    for user in listaUsuarios:
        print(user)

def alterarDadosUser(listaUsuarios):
    pesq = input('Digite o CPF do usuário que deseja alterar: ')
    for usuario in listaUsuarios:
        if (pesq == usuario[1]):
            print(usuario)
            alterar = input('Se deseja alterar o nome digite 1, se deseja alterar o e-mail digite 2.\nPara cancelar digite 3.\n')
            
            if (alterar == '1'):
                novoNome = input('Digite o novo nome: ')
                usuario[0] = novoNome
                print('Nome alterado com sucesso!')
                print(usuario)
                desejo = input('Deseja alterar o e-mail? s/n ').upper()
                if (desejo == 'S'):
                    novoEmail = input('Digite o novo e-mail: ')
                    usuario[2] = novoEmail
                    print('E-mail alterado com sucesso!')
                    print(usuario)
                else:
                    continue
            elif (alterar == '2'):
                novoEmail = input('Digite o novo e-mail: ')
                usuario[2] = novoEmail
                desejo2 = input('Deseja alterar o nome? s/n  ').upper()
                if (desejo2 == 'S'):
                    novoNome = input('Digite o novo nome: ')
                    usuario[0] = novoNome
                    print('Nome alterado com sucesso!')
                    print(usuario)
                else:
                    continue
            elif (alterar == '3'):
                break


def pesquisarUsuarioPeloCpf(listaUsuarios):
    pesq = input('Digite o CPF do usuário que deseja pesquisar: ')
    for usuario in listaUsuarios:
        if (pesq == usuario[1]):
            print('O usuário com o CPF ''"',pesq,'"' ,'é:' ,usuario[0])
    if (pesq != usuario[1]):
        print('Usuário não encontrado')

def cadastrarGasto(listaGastos):
    listaUnica = []
    gastos = input('Digite o novo gasto no formato:\n'
                   'tipo,descrição,dia do gasto,mês do gasto (1-12),ano do gasto,valor gasto,CPF do usuário\n')
    gastosUsuario = gastos.split(",")
    listaGastos.append(gastosUsuario)
    listaUnica.append(gastosUsuario)
    print('Gasto adicionado com sucesso!')
    print(listaUnica)
    
def listarGastosPeloCpf(listaGastos):
    cpfPesq = input('Digite o CPF do usuário para listar seu(s) gasto(s):\n')
    gCount = 0
    gastoTotal = 0.0
    lista = []
    for gasto in listaGastos:
        if (cpfPesq == gasto[6]):
            gCount += 1
            ln = (gasto[0]+' data: '+gasto[2]+'/'+gasto[3]+'/'+gasto[4]+' no valor: R$' +gasto[5])
            lista.append(ln)
            gastoTotal += float(gasto[5])
            if (gCount > 1):
                print('Os gastos encontrados para o CPF ',cpfPesq,'foram:')
                for k in lista:
                    print(k)
    if (gCount == 1):
        print('O gasto encontrado para o CPF',cpfPesq,'foi: Tipo = ' +gasto[0]+' data: '+gasto[2]+'/'+gasto[3]+'/'+gasto[4]+' no valor: R$' +gasto[5])
    print('Total gasto pelo usuário = R$',gastoTotal)
    if (cpfPesq != gasto[6]):
        print('Usuário não encontrado')

def listarGastos(listaGastos):
    print('Os seguintes gastos estão cadastrados:\n')
    for k in listaGastos:
        print(k)
        
def pesqGastoDespesaUsuario(listaGastos):
    pesqGCpf = input('Digite o CPF do usuário')
    somaGasto = 0.0
    gasto = ''
    tipoGasto = input('Digite o tipo da despesa: ')
    gasto = tipoGasto
    for user in listaGastos:
        if (pesqGCpf == user[6] and tipoGasto == user[0]):
            somaGasto += float(user[5])
    if (somaGasto == 0.0):
        print('Para o CPf' ,pesqGCpf, 'não foi encontrado nenhuma despesa do tipo' ,gasto)
    else:
        print('O total gasto pelo usuário com CPF' ,pesqGCpf, 'com',gasto, 'foi' ,somaGasto)

def totalUsuarios(listaUsuarios):
    print('O total de usuário cadastrados é: ' ,len(listaUsuarios))

def somaDespesasMes(listaGastos):
    somaDespesasMes = 0.0
    cpfPesqNew = input('Digite o CPF do usuário:\n')
    mesPesq = input('Digite o mês da despesa\n')
    anoPesq = input('Digite o ano da despesa\n')
    for user in listaGastos:
        if (cpfPesqNew == user[6] and mesPesq == user[3] and anoPesq == user[4]):
            somaDespesasMes += float(user[5])
    print('No mês' ,mesPesq, 'ano' ,anoPesq, 'o usuário com CPF' ,cpfPesqNew, 'gastou um total de: ' ,somaDespesasMes)

