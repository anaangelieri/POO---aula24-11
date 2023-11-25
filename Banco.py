#Conta_juca é um objeto que pertence a classe ContaCorrente
from Agencia import ContaCorrente

conta_juca = ContaCorrente('Juca', '123.456.789-12', '456', '789456123')
print('Saldo da Conta = ', conta_juca.saldo)
print('Cliente =', conta_juca.nome)
print('CPF =', conta_juca.cpf)
conta_juca.consultar_saldo()

conta_juca.depositar_dinheiro(10000)
conta_juca.consultar_saldo()
#conta_juca.sacar_dinheiro(1000)
#conta_juca.consultar_saldo()
conta_juca.sacar_dinheiro(7500)
conta_juca.consultar_saldo()
conta_juca.consultar_historico_transacoes()


conta_mae_juca = ContaCorrente('Jaca', '789.456.123-01', '456', '80100')
print('Saldo da Conta = ', conta_mae_juca.saldo)
print('Cliente =', conta_mae_juca.nome)
print('CPF =', conta_mae_juca.cpf)
conta_juca.transferir(1000, conta_mae_juca)
conta_mae_juca.consultar_saldo()
conta_mae_juca.consultar_historico_transacoes()