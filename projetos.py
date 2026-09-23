"""nome=input("Digite o seu nome:")
senha=input("Digite sua senha:")
if nome.lower()=="gustavo" and senha=="202524":
    print("Acesso liberado")
else:
    print("Acesso negado")"""
tentativa=0
tentativas=3
acesso = False
print("Digite seu loguin e senha, você terá ",tentativas,"tentativas")

while tentativa <3:
    tentativa+=1
    nome=input("Digite o seu nome:")
    senha = input("Digite sua senha:")


    if nome.lower()=="gustavo" and senha =="202524":
        acesso=True
        print("Acesso liberado")
        break
    else:
            print("Acesso negado,tente novamente ")

            tentativas -= 1
            print("Você tem agora: ",tentativas,"Tentativas ")
    if tentativas ==1:
            print("Atenção! Está é a sua ultima tentativa")
    elif tentativas ==0:
        print("conta bloqueada")
if not acesso:
    print("Acesso bloqueado")


