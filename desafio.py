from datetime import datetime, date, time
import pytz
import random

#variaveis

saldo = 1500
limite = 1000
extrato = ''
numero_saques = 0
limite_saques = 3


#horario e fuso

d = datetime.now(pytz.timezone("America/Sao_Paulo"))
mascara_ptbr = "%d/%m/%Y %H:%M"

# funções fincanceiras

def saque(saldo, numero_saques, limite_saques, limite, extrato):
    valor = float(input('Quanto deseja sacar?:'))

    if valor > saldo:
        print('Saldo insuficiente.')
        
    elif valor > limite:
        print('Limite insuficiente!')

    elif valor < saldo and numero_saques >= limite_saques:
        print('Número de saques diários atingidos, tente novamente amanhã.')

    else:
        saldo -= valor
        numero_saques += 1
        print(f'Saque realizado no valor de R${valor:.2f}.')
        extrato += f'Saque R${valor:.2f} realizado às {d.strftime(mascara_ptbr)}\n'

    return saldo, numero_saques, extrato

def deposito(saldo, extrato):
    valor = float(input('Qual valor será depositado?:'))
    saldo += valor
    print(f'Deposito no valor de R${valor:.2f}, realizado!')
    print(f'Saldo atual em R${saldo:.2f}.')
    extrato += f'Deposito R${valor:.2f} realizado às {d.strftime(mascara_ptbr)}\n'
    return saldo, extrato

def extratos_bancarios(saldo, extrato):
        print("\n ==========EXTRATO==========")
        print(extrato if extrato else "Não foi realizado nenhuma movimentação")
        print(f"Saldo: R${saldo:.2f}")
        print("====================")

                    #clientes

    #listas
clientes = []
contas_correntes = []

    #classes

class cliente:
    def __init__(self, nome, cpf, endereco):
         self.nome = nome
         self.endereco = endereco
         self.cpf = cpf

class contascorrente:
     def __init__(self, agencia, numero_conta, usuario, senha, cpf):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.login = usuario
        self.senha = senha
        self.cpf = cpf

    #funções

def criar_usuario():
        criacao = input ('Deseja criar usuario?:')
        if criacao in ['sim', 'Sim', 's']:
            cadastro_nome = input('Nome completo:')
            cadastro_cpf = input('CPF:')
            cadastro_endereco = input('Endereço:')

            if any(c.cpf == cadastro_cpf for c in clientes):
                print('CPF já cadastrado!')
                return criar_usuario()

            else:
                novo_cliente = cliente(cadastro_nome, cadastro_cpf, cadastro_endereco)
                clientes.append(novo_cliente)
                print(f'Conta criada com sucesso, {cadastro_nome}!')
                conta_corrente()
        else:
             login()
    
#    else:
#        cpf = input('Digite seu CPF: ')
#        cliente_existente = next((c for c in clientes if c.cpf == cpf), None)
#        if cliente_existente:
#            menu(saldo, numero_saques, extrato, limite_saques, limite)
#        else:
#            print("Cliente não encontrado!")
#            return criar_usuario()

def conta_corrente():
    agencia = "0001"
        
    usuario = input('Tem conta de usuario?:')
    if usuario.lower() in ["n", "não", "nao", "Não", "Nao"]:
        criar_usuario()
    else:
        confirmacao = input('Deseja criar conta corrente?:')
        if confirmacao.lower() in ['sim', 'Sim', 's']:
            cpf = input('Insira o do usuario CPF:')
            clientes_existentes = next((c for c in clientes if c.cpf == cpf), None) 
            if not clientes_existentes:
                print('Nenhum usuario encontrado.')
                return criar_usuario()
            
            numero_conta = random.randint(100000, 999999)
            usuario_login = input('Criar login: ')
            if any (c.login == usuario_login for c in contas_correntes):
                print('Esse login já existe.')
                return conta_corrente()
            else:
                usuario_senha = input('Criar senha: ')
                nova_conta = contascorrente(agencia, numero_conta, usuario_login, usuario_senha, cpf)
                contas_correntes.append(nova_conta)
                print(f'Conta criada com sucesso! Agência: {agencia} Conta: {numero_conta}')
                login()
        else:
             return login()

# função menu

def login():
    pag_inicial = input('Você já tem conta corrente?: ')
    if pag_inicial.lower() in ['n', "não", "nao", "Não", "Nao"]:
         conta_corrente()
    else:
        pag_inicial.lower() in ["s", "sim", "Sim"]
        contas = input('Deseja criar outra?:')
        if contas in ['sim', 'Sim', 's']:
             conta_corrente()
        else:
            usuario_login = input('Insira o login: ')
            usuario_senha = input('Insira a sua senha: ')
        if not contas_correntes:
            print('Usuario não encontrado.')
            return login()
        else:
            menu(saldo, numero_saques, extrato, limite_saques, limite)
        
         

def menu(saldo, numero_saques, extrato, limite_saques, limite):
    menu = """
    
    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair do sistema

    => """
    while True:
        opcao = input(menu)
            
        if opcao == "s":
                saldo, numero_saques, extrato = saque(saldo, numero_saques, limite_saques, limite, extrato)

        elif opcao == "d":
                saldo, extrato = deposito(saldo, extrato)
            
        elif opcao == "e":
                saldo = extratos_bancarios(saldo, extrato)

        elif opcao == "q":
                print("Saindo...")
                login()
        
        else:
                print("Opção inválida! tente novamente.")

#sistema rodando
#menu(saldo, numero_saques, extrato, limite, limite_saques)
login()
