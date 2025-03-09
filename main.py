from abc import ABC, abstractclassmethod, abstractmethod
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
      if self.saldo >= valor:
          self.saldo -= valor  # Atualiza o saldo corretamente
          return True  # Confirma o saque
      else:
          print("Saldo insuficiente!")  # Mensagem de erro
          return False  # Indica que o saque não foi realizado


     


      
      

    

    
  
  
    

  
  