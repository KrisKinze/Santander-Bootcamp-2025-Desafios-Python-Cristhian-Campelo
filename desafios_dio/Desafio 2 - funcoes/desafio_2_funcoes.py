import textwrap

# ======================== FUNCOES INCIAIS ===============================

def menu():
    texto_menu = """\n
    ================== MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [lu]\tListar usuários
    [bc]\tBusca contas por CPF
    [q]\tSair
    => """
    return input(textwrap.dedent(texto_menu))


#========================= FUNCOES DE OPERACOES ==========================
def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):

    if saldo <= 0 or valor > saldo:
        return extrato, saldo, numero_saques, False, "Saldo insuficiente"
        
    
    elif (numero_saques + 1) > limite_saques:
        return extrato, saldo, numero_saques, False, "Limite de saques diários alcançado, tente novamente amanhã"
        
    
    elif valor > limite:
        return extrato, saldo, numero_saques, False, f"Valor inserido ultrapassa o limite de saque, sendo o limite de R${limite}."
        
    
    else:
        saldo -= valor
        extrato += f"\nSaque de R${valor:.2f}. \n Novo saldo: R${saldo:.2f}\n"
        numero_saques += 1

        return extrato, saldo, numero_saques, True, ""

def depositar(saldo, valor, extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"\nDeposito de R${valor:.2f}. \n Novo saldo de: R${saldo:.2f}\n"

        return extrato, saldo, True, ""
    
    else:
        return extrato, saldo, False, f"Valor digitado (R${valor}) inválido."
    
def visualizar_historico(saldo,/,*,extrato):
    
    print(extrato)
    print(f" Saldo Final: R${saldo:.2f} \n")

# ========================= FUNCOES NOVAS ========================


def criar_usuario(nome, data_nascimento, cpf, endereco, usuarios):


    if not cpf.isdigit():
        return False, "CPF deve conter apenas números"

    elif any(usuario["cpf"] == cpf for usuario in usuarios):
        return False, "CPF já cadastrado em nossos sistemas."

    else:
        novo_usuario = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        }

        usuarios.append(novo_usuario)
        return True, "", novo_usuario

def criar_conta_corrente(contas, agencia, numero_conta, cpf, usuarios):
    
    usuario_encontrado = None

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        return False, "Usuário não encontrado, não foi possivel criar a conta.", {}, numero_conta   

    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario_cpf": usuario_encontrado["cpf"]
    }

    contas.append(nova_conta)
    numero_conta += 1
    return True, "Conta criada com sucesso", nova_conta, numero_conta

def listar_contas_por_cpf(cpf, contas, usuarios):
    
    if not cpf.isdigit():
        print("CPF deve conter apenas números.")
        return
    
    
    contas_usuario = [conta for conta in contas if conta["usuario_cpf"] == cpf]
    
    if not contas_usuario:
        print(f"Não foram encontradas contas para o CPF {cpf}")
    else:
        usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
        nome = usuario["nome"] if usuario else "Usuário não encontrado"
        
        print(f"\n===== CONTAS DO USUÁRIO: {nome} (CPF: {cpf}) =====")
        for conta in contas_usuario:
            print(f"Agência: {conta['agencia']} | C/C: {conta['numero_conta']}")
        print("============================================")

# ========================= FUNCAO PRINCIPAL ==========================



def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0

    while True:

        opcao = menu()

        if opcao == "d": #Deposito
            
            valor = int(input("Digite o valor que deseja depositar: "))
            extrato, saldo, sucesso, mensagem = depositar(saldo, valor, extrato)
            
            if sucesso:
                print("Operação realizada com sucesso!")
                print(f"Saldo atual: R${saldo:.2f}")

            else:
                print(f"ERRO: {mensagem}")


        elif opcao == "s": #Saque
            valor = int(input("Digite o valor que deseja sacar: "))
            extrato, saldo, numero_saques, sucesso, mensagem = sacar(saldo = saldo, valor = valor, extrato = extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            
            if sucesso:
                    print("Operação realizada com sucesso!")
                    print(f"Saldo atual: R${saldo:.2f}")

            else:
                print(f"ERRO: {mensagem}")


        elif opcao == "e": #Extrato
            visualizar_historico(saldo, extrato=extrato)

        elif opcao == "nc": #Nova conta
            cpf = input("Digite o CPF de um usuário já cadastrado (apenas números): ")

            resultado, mensagem, nova_conta, numero_conta = criar_conta_corrente(contas=contas, agencia=AGENCIA, numero_conta=numero_conta, cpf=cpf, usuarios=usuarios)

            if resultado:
                print(f"{mensagem}\n {nova_conta}\n")

            else:
                print(mensagem)

        elif opcao == "lc": #Listar contas...
            if not contas:
                print("Não há contas cadastradas...")

            else:
                print("\n================ CONTAS CADASTRADAS ================")
                for conta in contas:
                    cpf = conta["usuario_cpf"]
                    # Encontrar o usuário pelo CPF
                    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
                    nome = usuario["nome"] if usuario else "Usuário não encontrado"
                    
                    print(f"Agência: {conta['agencia']} | "
                        f"C/C: {conta['numero_conta']} | "
                        f"Titular: {nome} | "
                        f"CPF: {cpf}")
                print("=====================================================")

        elif opcao == "nu": #Novo usuario

            nome = input("Digite seu nome:")
            data_nascimento = input("Digire sua data de nascimento no formato dd/mm/aaa:")
            cpf = input("Digite seu cpf, apenas números:")
            endereco =""
            endereco_logradouro = input("Digite o nome do seu logradouro:")
            endereco_nro = input("Digite o número do seu endereço:")
            endereco_bairro = input("Digite o bairro do seu endereço:")
            endereco_cidade = input ("Digite a cidade de seu endereço:")
            endereco_sigla_estado = input("Digite a sigla do seu estado:")

            endereco = f"{endereco_logradouro}, {endereco_nro} - {endereco_bairro} - {endereco_cidade}/{endereco_sigla_estado}."
            
            resultado, mensagem, novo_usuario = criar_usuario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco, usuarios=usuarios)
            
            if resultado:
                print(f"\n {mensagem} \n {novo_usuario}")

            else:
                print(mensagem)

        elif opcao == "bc":  # Buscar contas por CPF
            cpf = input("Digite o CPF do usuário (apenas números): ")
            listar_contas_por_cpf(cpf, contas, usuarios)
                
        elif opcao == "lu": #Listar usuários
            
            if not usuarios:
                print("Não há usuários cadastrados...")

            else:
                print(usuarios)


        elif opcao == "q": #Sair
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()