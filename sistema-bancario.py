menu = """
[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair
==========> informe aqui: """

saldo = 0
limite_saque = 500
extrato_saque = []
extrato_deposito = []
num_saques = 0
LIMITE_SAQUES = 3

print(saldo)


while True:
    opcao = input(menu)
    
    if (opcao == "1"):
        valor = float(input("Informe o valor do saque: "))
        if(num_saques > LIMITE_SAQUES):
            print("Você não pode realizar mais saques hoje!")
        elif(valor <= 0):
            print("Valor inválido!")
        elif(valor > limite_saque):
            print("Você não tem saldo suficiente!")
        elif (valor > saldo):
            print("você não tem saldo suficiente")
        else:
            num_saques+=1
            saldo -= valor
            saldo_formatado = f"{saldo:.2f}"
            extrato_saque.append(f"Saque: R${valor:.2f}")
            print(f"saldo atual: {saldo_formatado}")
    elif(opcao == "2"):
        valor = float(input("Informe o valor do depósito: "))
        if(valor <= 0):
            print("Valor inválido!")
        else:
            saldo += valor
            deposito_formatado = f"{valor:.2f}"
            extrato_deposito.append(f"Depósito: R${deposito_formatado}")
    elif(opcao == "3"):
        if(not extrato_saque and not extrato_deposito):
            print("Você não tem movimentações!")
        for deposito in extrato_deposito:
            print(deposito)
        for saque in extrato_saque:
            print(saque)
    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
