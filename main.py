import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

# Classe Cliente representa um cliente genérico, armazenando endereço e contas.
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica herda de Cliente e adiciona informações específicas de uma pessoa física.
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# Classe Conta representa uma conta bancária genérica.
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        conta = cls(numero, cliente)
        cliente.adicionar_conta(conta)
        return conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        if valor > self._saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True

        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False

# Classe ContaCorrente adiciona limite e controle de saques.
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = sum(1 for t in self.historico.transacoes if t["tipo"] == "Saque")

        if valor > self._limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False

        if numero_saques >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""
            Agência:   {self.agencia}
            C/C:       {self.numero}
            Titular:   {self.cliente.nome}
        """

# Classe Historico armazena transações realizadas na conta.
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {"tipo": transacao.__class__.__name__, "valor": transacao.valor, "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
        )

# Classe abstrata Transacao define a estrutura de uma transação.
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Saque representa a operação de saque.
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

# Classe Deposito representa a operação de depósito.
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

# Função menu exibe as opções disponíveis.
def menu():
    opcoes = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(opcoes))

# Função filtrar_cliente busca um cliente pelo CPF.
def filtrar_cliente(cpf, clientes):
    return next((cliente for cliente in clientes if cliente.cpf == cpf), None)

# Função recuperar_conta_cliente retorna a primeira conta do cliente.
def recuperar_conta_cliente(cliente):
    return cliente.contas[0] if cliente.contas else None

# Função criar_cliente adiciona um novo cliente.
def criar_cliente(clientes):
    cpf = input("Informe o CPF: ")
    if filtrar_cliente(cpf, clientes):
        print("\n@@@ CPF já cadastrado! @@@")
        return

    clientes.append(PessoaFisica(
        nome=input("Nome: "),
        data_nascimento=input("Data de nascimento (dd-mm-aaaa): "),
        cpf=cpf,
        endereco=input("Endereço: ")
    ))
    print("\n=== Cliente criado com sucesso! ===")

# Função criar_conta adiciona uma nova conta ao cliente.
def criar_conta(numero_conta, clientes, contas):
    cliente = filtrar_cliente(input("CPF do cliente: "), clientes)
    if cliente:
        contas.append(ContaCorrente.nova_conta(cliente, numero_conta))
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Cliente não encontrado! @@@")

# Função main gerencia o fluxo do programa.
def main():
    clientes, contas = [], []

    while (opcao := menu()) != "q":
        if opcao == "d":
            pass  # Implementar depósito
        elif opcao == "s":
            pass  # Implementar saque
        elif opcao == "e":
            pass  # Implementar extrato
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            criar_conta(len(contas) + 1, clientes, contas)
        elif opcao == "lc":
            for conta in contas:
                print(conta)
        else:
            print("\n@@@ Opção inválida! @@@")

main()