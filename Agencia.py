from datetime import datetime
import pytz

#Criação da classe Conta Corrente

class ContaCorrente:
    '''
        A classe ContaCorrente simula o funcionamento de uma Conta Corrente real
    '''
# Contrutor da classe ContaCorrente
    def __init__(self, nome, cpf, agencia, num_conta):
#Atributos da classe
#saldo inicia dentro da classe e é manipulado dentro dela
#um underline antes de cpf quer dizer que não poderá ser alterado
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual = R${:,.2f}'.format(self.saldo))

#Método para depositar valores
    def depositar_dinheiro(self, valor):
        self.saldo += valor
        # self.saldo = self.saldo + valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
#é colocado mais um parênteses para transformar valor, saldo, data e hora dentro de uma tupla, o que não seria possível sem eles pq o append só funciona para uma única informação, e a tupla será adicionada a lista transacoes

#Método para sacar valores
    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor.')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def limite_conta(self):
        self.limite = -1000
        return self.limite

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def consultar_historico_transacoes(self):
        print('Histórico de transações')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))
