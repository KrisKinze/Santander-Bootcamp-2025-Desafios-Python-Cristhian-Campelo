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

# ========================= FUNCOES NOVAS =============================


def criar_usuario(nome, data_nascimento, cpf, endereco, usuarios):

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    return True, "\nUsuário criado com sucesso.\n", novo_usuario

def criar_conta_corrente(contas, agencia, numero_conta, cpf, usuarios):
    
    usuario_encontrado = None

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        return False, "\nUsuário não encontrado, não foi possivel criar a conta.\n", {}, numero_conta   

    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario_cpf": usuario_encontrado["cpf"],
        "nome_conta": usuario_encontrado["nome"]
    }

    contas.append(nova_conta)
    numero_conta += 1
    return True, "Conta criada com sucesso", nova_conta, numero_conta

def listar_contas_por_cpf(cpf, contas, usuarios):
    
    if not cpf.isdigit():
        print("=" *30)
        print("\nCPF deve conter apenas números.\n")
        print("=" *30)
        return
    
    
    contas_usuario = [conta for conta in contas if conta["usuario_cpf"] == cpf]
    
    if not contas_usuario:
        print("=" *30)
        print(f"\nNão foram encontradas contas para o CPF: {cpf}\n")
        print("=" *30)
        return
    else:
        usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
        nome = usuario["nome"] if usuario else "Usuário não encontrado"
        
        print(f"\n=============== CONTAS DO USUÁRIO: {nome} (CPF: {cpf}) ===============")
        print("")
        for conta in contas_usuario:
            print(f"Agência: {conta['agencia']} \n C/C: {conta['numero_conta']}\n")
        print("")
        print("=" * 50)

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
    numero_conta = 1

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
            print("=" * 50)
            resultado, mensagem, nova_conta, numero_conta = criar_conta_corrente(contas=contas, agencia=AGENCIA, numero_conta=numero_conta, cpf=cpf, usuarios=usuarios)

            if resultado:
                    print(mensagem)
                    print("")
                    print(f"CPF da Conta: {nova_conta["usuario_cpf"]}")
                    print(f"Titular: {nova_conta["nome_conta"]}")
                    print(f"Agência: {nova_conta["agencia"]}")
                    print(f"C/C: {nova_conta["numero_conta"]}")
                    
            else:
                print(mensagem)
            print("=" * 50)


        elif opcao == "lc": #Listar contas...
            if not contas:
                print("=" *30)
                print("\nNão há contas cadastradas...\n")
                print("=" *30)

            else:
                print("\n================ CONTAS CADASTRADAS ================")
                for conta in contas:
                    cpf = conta["usuario_cpf"]
                    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
                    nome = usuario["nome"] if usuario else "Usuário não encontrado"
                    
                    print(f"Agência: {conta['agencia']} \n "
                        f"C/C: {conta['numero_conta']} \n "
                        f"Titular: {nome} \n "
                        f"CPF: {cpf}\n")
                print("=====================================================")

        elif opcao == "nu": #Novo usuario

            cpf = input("Digite seu cpf, apenas números:")

            if any(usuario["cpf"] == cpf for usuario in usuarios):
                print("=" *30)
                print("\nNão foi possivel criar o usuário. CPF já cadastrado em nossos sistemas.\n")
                print("=" *30)

            elif not cpf.isdigit():
                print("=" *30)
                print("\nCPF deve conter apenas números\n")
                print("=" *30)


            else:
                nome = input("Digite seu nome:")
                data_nascimento = input("Digire sua data de nascimento no formato dd/mm/aaa:")
                endereco =""
                endereco_logradouro = input("Digite o nome do seu logradouro:")
                endereco_nro = input("Digite o número do seu endereço:")
                endereco_bairro = input("Digite o bairro do seu endereço:")
                endereco_cidade = input ("Digite a cidade de seu endereço:")
                endereco_sigla_estado = input("Digite a sigla do seu estado:")

                endereco = f"{endereco_logradouro}, {endereco_nro} - {endereco_bairro} - {endereco_cidade}/{endereco_sigla_estado}."
                
                resultado, mensagem, novo_usuario = criar_usuario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco, usuarios=usuarios)
            
                if resultado:
                    print("=" * 30)
                    print(mensagem)
                    print("")
                    print(f"Nome: {novo_usuario["nome"]}")
                    print(f"Data de Nascimento: {novo_usuario["data_nascimento"]}")
                    print(f"CPF: {novo_usuario["cpf"]}")
                    print(f"Endereço: {novo_usuario["endereco"]}")
                    print("=" * 30)


                else:
                    print(mensagem)

        elif opcao == "bc":  # Buscar contas por CPF
            cpf = input("Digite o CPF do usuário (apenas números): ")
            listar_contas_por_cpf(cpf, contas, usuarios)
                
        elif opcao == "lu": #Listar usuários
            
            if not usuarios:
                print("\nNão há usuários cadastrados...\n")

            else:
                print("========================= LISTA DE USUÁRIOS =========================")
                for usuario in usuarios:
                    print("=" * 50)
                    print(f"Nome: {usuario["nome"]}")
                    print(f"Data de Nascimento: {usuario["data_nascimento"]}")
                    print(f"CPF: {usuario["cpf"]}")
                    print(f"Endereço: {usuario["endereco"]}\n")
                    print("=" * 30)


        elif opcao == "q": #Sair
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()