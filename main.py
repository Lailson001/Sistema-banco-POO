
from datetime import datetime



class Cliente:
  def __init__(self, endereço):
    self.endereço = endereço
    self.contas = []


def realizar_transacao(self, conta, transacao):
  transacao.registrar(conta)

def adicionar_conta(self, conta):
  self.contas.append(conta)  

class cliente(Cliente):
  def __init__(self, nome,data_nascimento, cpf, endereço):
    super().__init__(endereço)
    self.nome = nome
    self.data_nascimento = data_nascimento
    self.cpf = cpf

class Conta:
  def __init__(self, numero , saldo, cliente):
    self._saldo = 0
    self._numero = numero
    self._agencia = "0001"
    self._cliente = cliente
    self._transacoes = []
    self._historico = historico()
    
    @classmethod
    def criar_conta(cls, numero, saldo, cliente):
      return cls(numero, saldo, cliente)
      
    @property
    def saldo(self):
      return self._saldo
      
    @property 
    def numero(self):
      return self._numero

    @property
    def agencia(self):
     return self.cliente
      
    @property
    def cliente(self):
      return self._cliente
      
    @property
    def hitorico(self):
      return self._historico
      
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
          print(f"Saldo insuficiente. Saldo disponível: {saldo}")

        elif valor > 0:
          self.saldo -= valor
          print(f"Saque de {valor} realizado com sucesso. Saldo restante: {self.saldo}")
          return True

        else:
          print("Valor inválido para saque.")
          return False

    def depositar(self, valor):
        if valor > 0:
          self.saldo += valor
          print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {self.saldo}")
          return True

        else:
          print("Valor inválido para depósito.")
          return False


  class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self._transacoes if transacao.tipo == "saque"]
        )

        excedeu_limite = numero_saques >= self._limite_saque

        if excedeu_limite:
            print("Limite de saques excedido.")
            return False

        else:
          return super().sacar(valor)


def __str__ (self):
  return f"Conta {self._numero} - Saldo: {self._saldo}"

class

      
       
       
       
       
         
    

         
       





      
     

           


     


      
      

    

    
  
  
    

  
  