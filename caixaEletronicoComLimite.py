#Declarando variavel
valorDoSaque=0
saldoInicial=1000
limitePorSaque=500
while   saldoInicial>0:
    valorDoSaque = int(input("Digite o valor do saque:"))

    if valorDoSaque>limitePorSaque:
        print("saque não autorizado, limite de saque R$500")

    elif valorDoSaque>saldoInicial :
        print("saque não autorizado, saldo indisponivel")
    elif valorDoSaque <=0:
        print("Digite um valor positivo ")
    else:
        saldoInicial = saldoInicial - valorDoSaque
        print("saque autorizado")
        print("saldo da conta R$", saldoInicial)
        print("valor retirado",valorDoSaque)

