#Declaração de variaveis
saldoInicial=1000
saqueSolicitado=0
while not saldoInicial==0:
    saqueSolicitado = int(input("Digite o valor que deseja sacar R$:"))
    if saqueSolicitado<=0:
        print("Valor invalido")

    elif saqueSolicitado >saldoInicial:
        print("saldo insuficiente")
    else :
        saldoInicial = saldoInicial - saqueSolicitado


        print("Saque realizado no valor de R$",saqueSolicitado)
        print("Valor Restante:R$",saldoInicial)

print("Acabaram as possibilidades")




