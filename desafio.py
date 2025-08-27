#variaveis

saldo = 1500
limite = 1000
extrato = ''
numero_saques = 0
limite_saques = 3

menu = """

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair do sistema

=> """

# funções

def saque(saldo, numero_saques, limite_saques, limite, extrato):
    valor = float(input('Quanto deseja sacar?:'))

    if valor > saldo:
        print('Saldo insuficiente.')
        
    elif valor < saldo and valor > limite:
        print('Limite insuficiente!')

    elif valor < saldo and numero_saques >= limite_saques:
        print('Número de saques diários atingidos, tente novamente amanhã.')

    else:
        saldo -= valor
        numero_saques += 1
        print(f'Saque realizado no valor de R${valor:.2f}.')
        extrato += f'Saque R${valor:.2f} realizado'

    return saldo, numero_saques, extrato
    
def deposito(saldo, extrato):
    deposito = float(input('Qual valor será depositado?:'))
    saldo += deposito
    print(f'Deposito no valor de R${deposito}, realizado!')
    print(f'Saldo atual em R${saldo}.')
    extrato += f'Deposito R${deposito:.2f} realizado '
    return saldo, extrato

while True:
    opcao = input(menu)

    if opcao == "s":
        saldo, numero_saques, extrato = saque(saldo, numero_saques, limite_saques, limite, extrato)

    elif opcao == "d":
        saldo = deposito(saldo, extrato)
    
    elif opcao == "e":
        print("\n ==========EXTRATO==========")
        print(extrato if extrato else "Não foi realizado nenhuma movimentação")
        print(f"Saldo: R${saldo:.2f}")
        print("====================")

    elif opcao == "q":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida! tente novamente.")