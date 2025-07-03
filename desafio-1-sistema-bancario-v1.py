import sys
import textwrap

saldo = 10.0
depositos = ""
saques = ""


# INICIO DOS MENUS =================================

opcao = -1
menu_princcipal = """
======================MENU==========================

Seja muito bem vindo ao menu inicial!
Por favor escolha uma das opções para proseguir:

(0) Fechar Menu
(1) Realizar um deposito
(2) Realizar um saque
(3) Verificar extrato
====================================================
\n
"""

menu_deposito = """   
======================DEPOSITO======================

Opcao de deposito Selecionada!
Por favor digite o valor que deseja depositar:

====================================================
\n
"""
quantidade_de_saques_diarios_realizados = 0
limite_de_quantidade_de_saques_diarios = 3
limite_do_valor_de_saques_diarios = 500.00
menu_saque = """ 
======================SAQUE=========================

Opcao de saque Selecionada!
Por favor digite o valor que deseja sacar:

====================================================
\n
"""

# FIM DOS MENUS ====================================

# FUNCAO PARA PERGUNTAR AO USUARIO SOBRE O RETORNO AO MENU PRINCIPAL
def perguntar_retorno_menu():
    continuar = ""
    while True: 
        continuar = input("Deseja retornar ao menu inicial? s/n \n")
        
        if continuar == "n":
            print("Encerrando o programa...")
            sys.exit()
        elif continuar == "s": 
            print("Retornando ao menu...")
            return 
        else:
            print("Opção inválida. Por favor digite (s) para sim ou (n) para não...")

            # Apesar de não ter sido apresentado as funcoes até o momento desse desafio. Pesquisei e achei interessante implementar para esse caso.

#INICIO DA LOGICA DE PROGRAMACAO ===================

while opcao != 0 :

    opcao = int(input(menu_princcipal))

    print("")

    if opcao == 1 : #=========== Deposito ==========

        try:

            ultimo_deposito = float(input(menu_deposito))
        
        except ValueError:
            print("Valor inválido! Digite um número.")
        
        if ultimo_deposito < 0 :
            print("Valor inválido! Digite um número positivo.")

            print("")
            
            perguntar_retorno_menu()
            continue # Continue para poder retorna ao menu principal

        else:
            depositos += f"R$ {ultimo_deposito:.2f} \n"
            saldo += ultimo_deposito
            print(f"Deposito de R$ {ultimo_deposito:.2f} realizado com sucesso! \n")
            

            perguntar_retorno_menu()
            continue

    if opcao == 2 : #========== saque ==========


        if saldo <= 0:
            print("Nao sera possivel sacar o dinheiro por falta de saldo. Retornado ao menu principal... \n")
            continue
        

        else:

            ultimo_saque = float(input(menu_saque))

            if quantidade_de_saques_diarios_realizados >= limite_de_quantidade_de_saques_diarios:
                print("Limite de saques diarios alcancado. Por favor, tente novamente amanhã ou consulte seu banco. \n")
                continue

            elif ultimo_saque > limite_do_valor_de_saques_diarios:
                print(f"Você ultrapassou o valor limite para saque. Sendo ele de R$ {limite_do_valor_de_saques_diarios:.2f}.\n")
                print("Por favor, tente com um valor menor. Retornando ao menu principal...")
                continue

            elif ultimo_saque <= 0 :
                print("Valor digitado invalido. Por favor, digite um valor positivo e não nulo...")
                print("Retornando ao menu principal...")
                continue

            else:
                print(f"Saque de {ultimo_saque} realizado com sucesso! \n")
                saques += f"R$ {ultimo_saque:.2f} \n"
                quantidade_de_saques_diarios_realizados += 1
                saldo -= ultimo_saque

                perguntar_retorno_menu()
                continue   

    
    if opcao == 3 : #========== extrato ==========
        # Menu para Extratos atualizado. Movido para o final. Quando no começo, ele pegava os valores antes das alterações.
        menu_extrato = f"""======================EXTRATO=======================

Depositos realizados:
{depositos}

Saques realizados:
{saques}

Saldo atual da conta:
R$ {saldo:.2f}

====================================================
\n
"""  # Para manter a identacao e ao mesmo tempo alinhar o menu do EXTRATO, precisei identa o f-string dessa maneira.

        print(menu_extrato)

        perguntar_retorno_menu()
        continue

#==========SAINDO DO LOOP==========

# Caso seja selecionado a opção "0"
print("Fechando menu. Muito obrigado por utilizar nossos serviços! Aguardamos seu retorno.")

