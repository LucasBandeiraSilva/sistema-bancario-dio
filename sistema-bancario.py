menu = """
[1] Cadastrar usuario
[2] Cadastrar conta corrente
[3] Sacar
[4] Depositar
[5] Extrato
[6] Sair
==========> informe aqui: """

saldo = 0
limite_saque = 500
numero_da_conta = 0
num_saques = 0
TOTAL_SAQUES_DIARIOS = 3
AGENCIA = "0001"
usuarios_cadastrados = []
contas_bancarias_cadastradas =[]
extrato = []


def criar_usuario():
    nome = input("Informe seu nome: ")
    cpf = int(input("Informe seu CPF (somente números): "))
    if encontrar_usuario_por_cpf(cpf =cpf):
        print("O CPF já está cadastrado, por favor informe outro.")
        return None
    logradouro = input("informe o seu logradouro: ")
    numero = int(input("Informe o número do seu logradouro: "))
    bairro = input("Informe seu Bairro: ")
    cidade = input("Informe a sua cidade: ")
    sigla = input("Informe a sigla do seu estado: ")
    usuarios = {"nome":nome, 
                "cpf":cpf,
                "logradouro":logradouro, 
                "numero":numero, 
                "bairro":bairro, 
                "cidade":cidade, 
                "sigla": sigla,
                "Conta_Bancaria": None}
    usuarios_cadastrados.append(usuarios)
    print(usuarios_cadastrados)
    return usuarios

def encontrar_usuario_por_cpf(*,cpf):
    for usuario in usuarios_cadastrados:
        if usuario["cpf"] == cpf:
            return usuario
        print(usuario["cpf"])
    return False
    
def criar_conta_corrente(num_conta = numero_da_conta):
    cpf = int(input("Informe seu CPF (somente números): "))
    usuario = encontrar_usuario_por_cpf(cpf=cpf)
    if not usuario:
        print("CPF não encontrado, por favor cadastre-se.")
        return None
    
    conta_bancaria = {
        "agencia": AGENCIA,
        "numero_da_conta": num_conta+1
    }
    contas_bancarias_cadastradas.append(conta_bancaria)
    usuario["Conta_Bancaria"] = contas_bancarias_cadastradas
    print(f"Sua conta corrente foi cadastrada com sucesso {usuario["nome"]}! \n Dados da sua conta bancaria: {usuario}")
    return usuario

def gerar_extrato(saldo,/,*,extrato):
    cpf = int(input("Informe seu CPF (somente números): "))
    usuario = encontrar_usuario_por_cpf(cpf=cpf)
    if not usuario:
        print("CPF não encontrado, por favor cadastre-se.")
        return None
    if not extrato:
        return "Você não tem movimentações"
    print("Extrato: \n")
    print(f"Saldo atual: R$ {saldo}")
    for extrato in extrato:
        print(f"{extrato}")
        
def realizar_saque(*,num_saques,limite_saque,saldo,TOTAL_SAQUES_DIARIOS,extrato):
    valor = float(input("Informe o valor do saque: "))
    if num_saques == TOTAL_SAQUES_DIARIOS :
        print("Você atingiu o limite de saques diários.")
    elif valor <= 0:
        print("Valor inválido")
    elif valor > saldo:
        print("Saldo insuficiente")
    elif valor > limite_saque:
        print("Valor do saque maior que o limite diário")
    else:
        num_saques+=1
        saldo -= valor
        saldo_formatado = f"{saldo:.2f}"
        extrato.append(f"Saque: R${valor:.2f}")
        print(f"saldo atual: {saldo_formatado}")
    return saldo, extrato
while True:
    
    opcao = input(menu)
    
    if (opcao == "1"):
        criar_usuario()
    elif(opcao == "2"):
        
        criar_conta_corrente(num_conta= numero_da_conta)
        numero_da_conta+=1
    elif (opcao == "3"):
        realizar_saque(num_saques=num_saques,limite_saque=limite_saque,
                       saldo=saldo,TOTAL_SAQUES_DIARIOS=TOTAL_SAQUES_DIARIOS,
                       extrato=extrato)
    elif(opcao == "4"):
        valor = float(input("Informe o valor do depósito: "))
        if(valor <= 0):
            print("Valor inválido!")
        else:
            saldo += valor
            deposito_formatado = f"{valor:.2f}"
            extrato.append(f"Depósito: R${deposito_formatado}")
    elif(opcao == "5"):
        gerar_extrato(saldo,extrato=extrato)
    
    elif opcao == "6":
        print("Saindo do sistema. Até logo!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")

