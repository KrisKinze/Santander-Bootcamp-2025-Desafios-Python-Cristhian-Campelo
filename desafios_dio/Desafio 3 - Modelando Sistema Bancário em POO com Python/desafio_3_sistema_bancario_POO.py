from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime, UTC

#Comecando pelas interfaces e Classes Abstratas, irei implementar as funcoes posteriormente

class Transacao(ABC):
    @abstractmethod
    def registrar(self,Conta):
        pass
    
class Deposito(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Implementar depois // Implementando depois de criar as classes bases.
        retorno_transacao = conta.depositar(self.valor)

        if retorno_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        # Implementar depois // Implementando depois de criar as classes bases.
        retorno_transacao = conta.sacar(self.valor)

        if retorno_transacao:
            conta.historico.adicionar_transacao(self)

# Indo para Classes Bases e as Isoladas

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now(UTC).strftime("%d-%m-%Y %H:%M:%S"),  # Atualizado com a nova sintaxe do UTC
        })

    def transacoes_do_dia(self):
        data_atual = datetime.now(UTC).date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes

class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []


    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 10:
            print("\n@@@ Você excedeu o número de transações permitidas do dia. @@@")
            return
        
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento 

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    # Criando métodos com propety para consultar cada atributo (privado)

    @property
    def saldo (self): # Método Saldo()
        return self._saldo
    
    @property
    def numero (self):
        return self._numero
    
    @property
    def agencia (self):
        return self._agencia
    
    @property
    def cliente (self):
        return self._cliente
    
    @property
    def historico (self):
        return self._historico
    
    # Criando demais métodos

    @classmethod
    def nova_conta(cls,numero,cliente): 
        return cls(numero,cliente) # Conta(numero, cliente) - instanciando a classe Conta.

    def sacar(self, valor):
        
        if valor < 0 :
            print("\n@@@ Operação falhou! Valor digitado foi negativo. @@@")
            return False
        
        elif valor > self._saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        else:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
    
    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor digitado inválido. @@@")
            return False
        
        else:
            self._saldo += valor
            print("\n=== Deposito realizado com sucesso! ===")
            return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500.00, limite_saques=3): # Valores padroes de limites, posto nos desafios anteriores
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    

    def sacar(self, valor):

        numero_saques = len( # Usando o objeto self.historico para contar a quantidade de transacoes do tipo saque.
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__] 
        )

        if numero_saques >= self.limite_saques:
            print("\n@@@ Operação falhou! Limite de saques atingido. @@@")
            return False

        elif valor > self.limite:
            print("\n@@@ Operação falhou! Valor limite atingido. @@@")
            return False
        else:
            return super().sacar(valor) # Chamando o metodo sacar da classe pai (Conta.sacar) , e dentro dela já tem os devidos returns;


# A partir daqui, segue a realizacao do desafio extra. 

# Implementando o Menu

def menu():
    return """
    ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [nu] Novo usuário
    [lc] Listar contas
    [q]  Sair
    => 
    """

# Implementando Funcoes do Menu

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

def filtrar_cliente(cpf, clientes): # Funcao Auxiliar
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Ocorreu um erro. Cliente não encontrado! @@@")
        return

    numero_conta = len(contas) + 1
    conta = ContaCorrente.nova_conta(numero_conta, cliente)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\n=== Conta criada com sucesso! ===")

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n\tData: {transacao['data']}"
    
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def listar_contas(contas):
    if not contas:
        print("\n@@@ Não há contas cadastradas! @@@")
        return
    
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        print("=" * 50)
        print(f"Agência:\t{conta.agencia}")
        print(f"C/C:\t\t{conta.numero}")
        print(f"Titular:\t{conta.cliente.nome}")
        print(f"CPF:\t\t{conta.cliente.cpf}")
        print(f"Saldo:\t\tR$ {conta.saldo:.2f}")
        print(f"Limite:\t\tR$ {conta.limite:.2f}")
        print(f"Limite Saques:\t{conta.limite_saques}")
    print("=" * 50)

# Implementando funcao main
def main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nc":
            criar_conta(clientes, contas)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, selecione novamente a operação desejada. @@@")

if __name__ == "__main__":
    main()






