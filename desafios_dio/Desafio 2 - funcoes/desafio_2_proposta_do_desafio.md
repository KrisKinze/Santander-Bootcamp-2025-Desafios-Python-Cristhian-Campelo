# Criar funções para (Com regras na passada de argumentos):

- Sacar.
    - Keyword only - apenas por nome.
    - Sugestões de argumentos: saldo, valor, extrato, limite, número de saques, limite de saques.
    - Sugestão de Retorno: saldo e extrato.  

- Depositar.
    - Argumentos apenas por posição: positional only
    - Sugestão de argumentos: saldo, valor, extrato.
    - Sugestão de retorno: saldo e extrato.

- Visualizar histórico.
    - Argumentos por posição e nome: positional only e keyword only.
    - Argumentos posicionais: saldo.
    - Argumentos nomeados: extrato.

# além disso, 2 novas funções:


- Criar usuário (cliente do banco)
    - Armazenar os usuários em uma lista.

    - Usuário composto por: 
        - Nome.
        - Data de nascimento.
        - CPF
            - Devem ser armazenados somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.
        - Endereço.
            O endereço é uma string com o formato: logradouro, n.o - bairro - cidade/sigla estado.
    

- Criar conta-corrente (vincular com usuário)

    - Armazenar as contas em uma lista.

    A conta é composta por:
        - Agência.
            - O número da agência é fixo: "0001"
        - Número da conta.
            - O número da conta é sequencial, iniciando com 1.
        - Usuário.

    - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.


- Fique à vontade para adicionar mais funções, exemplo: listar contas.


# Dica.
- Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.