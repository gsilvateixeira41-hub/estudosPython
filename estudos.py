idade =int(input("Digite sua idade:"))

if idade >=18:
    print("Maior de idade")
elif idade >15 and idade <=17:
    print("Adolescente")
elif idade >0 and idade <=14:
    print("criança")