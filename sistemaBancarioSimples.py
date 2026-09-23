saldo=1000
saque=0
opcao=0
depositar=0
while opcao != 4:
    print("1- consultar saldo")
    print("2- saque")
    print("3- Depositar")
    print("4- Sair")
    opcao = int(input("Escolha uma opção:"))


    if opcao ==1:
        print("R$",saldo)

    elif opcao ==2:
        saque = int(input("Digite o valor do saque:"))

        if saque >saldo :
            print("saque negado")
        elif saque <=0:
            print("saque negado")
        else:
            saldo = saldo - saque
            print("saque autorizado")
            print("R$",saque)
    elif opcao ==3:
        depositar = int(input("Digite o valor do depositar:"))

        if depositar <=0:
            print("deposito negado")
        else:
            saldo=saldo+depositar
            print("deposito autorizado")
            print("R$",depositar)
    elif opcao ==4:
        print("Sair")
        break
    else:
        print("opção invalida")
print("Fim do programa")