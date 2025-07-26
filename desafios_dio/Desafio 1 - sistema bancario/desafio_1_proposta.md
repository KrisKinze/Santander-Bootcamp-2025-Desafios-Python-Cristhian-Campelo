# 🏛️ Proposta do Desafio 1 - Sistema Bancário Simples

## 🎯 **Objetivo**

Criar um sistema bancário básico em Python que simule operações bancárias fundamentais utilizando conceitos básicos de programação.

## 📋 **Requisitos Funcionais**

### **1. Operações Básicas**
- ✅ **Depósito**: Permitir depósitos de valores positivos
- ✅ **Saque**: Permitir saques com validações de limite
- ✅ **Extrato**: Exibir histórico de transações e saldo atual

### **2. Regras de Negócio**

#### **Depósitos:**
- Aceitar apenas valores positivos
- Não há limite para quantidade de depósitos
- Atualizar saldo automaticamente

#### **Saques:**
- **Limite de valor**: Máximo R$ 500,00 por saque
- **Limite de quantidade**: Máximo 3 saques por dia
- **Verificação de saldo**: Não permitir saque sem saldo suficiente
- Aceitar apenas valores positivos

#### **Extrato:**
- Exibir todos os depósitos realizados
- Exibir todos os saques realizados
- Mostrar saldo atual da conta
- Formato: R$ 0,00 (duas casas decimais)

### **3. Interface**
- Menu interativo em linha de comando
- Opções numeradas para cada operação
- Mensagens claras de sucesso/erro
- Opção para retornar ao menu ou sair

## 🛠️ **Especificações Técnicas**

### **Conceitos a Aplicar:**
- **Variáveis**: Para armazenar saldo, depósitos e saques
- **Estruturas condicionais**: `if`, `elif`, `else`
- **Loops**: `while` para menu principal
- **Tratamento de entrada**: Validação de dados do usuário
- **Formatação**: Uso de f-strings para exibição

### **Estrutura Sugerida:**
```python
# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Menu principal
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

# Loop principal
while True:
    opcao = input(menu)
    # Implementar operações...
```

## ✅ **Critérios de Avaliação**

### **Funcionalidade (40%):**
- Sistema executa sem erros
- Todas as operações funcionam corretamente
- Validações implementadas adequadamente

### **Lógica de Programação (30%):**
- Uso correto de estruturas condicionais
- Controle de fluxo adequado
- Tratamento de casos especiais

### **Organização do Código (20%):**
- Código limpo e legível
- Comentários quando necessário
- Nomes de variáveis descritivos

### **Interface do Usuário (10%):**
- Menu intuitivo e claro
- Mensagens informativas
- Experiência de usuário adequada

## 🎯 **Cenários de Teste**

### **Teste 1: Depósito Válido**
```
Entrada: Depositar R$ 100,00
Resultado: Saldo = R$ 100,00
```

### **Teste 2: Saque Válido**
```
Pré-condição: Saldo = R$ 100,00
Entrada: Sacar R$ 50,00
Resultado: Saldo = R$ 50,00, Saques restantes = 2
```

### **Teste 3: Saque Inválido - Valor Limite**
```
Entrada: Sacar R$ 600,00
Resultado: Erro - "Valor excede limite de R$ 500,00"
```

### **Teste 4: Saque Inválido - Quantidade**
```
Pré-condição: 3 saques já realizados
Entrada: Sacar R$ 100,00
Resultado: Erro - "Limite de saques diários atingido"
```

### **Teste 5: Extrato**
```
Histórico: Depósito R$ 100,00, Saque R$ 30,00
Resultado: Extrato mostra ambas operações e saldo R$ 70,00
```

## 🚀 **Diferencial (Opcional)**

- Validação robusta de entrada do usuário
- Formatação elegante do extrato
- Função para retorno ao menu principal
- Tratamento de exceções
- Mensagens de confirmação

## 📝 **Entrega**

- **Arquivo**: `sistema_bancario_simples.py`
- **Documentação**: Comentários no código explicando a lógica
- **Teste**: Sistema deve executar corretamente
- **Repositório**: Upload no GitHub com README explicativo

---

## 💡 **Dicas de Implementação**

1. **Comece simples**: Implemente uma operação por vez
2. **Teste frequentemente**: Execute o código após cada funcionalidade
3. **Valide entradas**: Sempre verificar se o usuário digitou valores válidos
4. **Use f-strings**: Para formatação de valores monetários
5. **Organize o código**: Separe as diferentes operações claramente