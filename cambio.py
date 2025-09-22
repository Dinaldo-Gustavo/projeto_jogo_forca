taxa = 5.33

def real_para_dolar(real):
    return real / taxa

def dolar_para_real(dolar):
    return taxa * dolar
while True:

    escolha = int(input("Você deseja converter R$ para U$(1) ou U$ para R$(2) (-1 para encerrar)? "))

    if escolha == -1:
        print("Programa encerrado!")
        break

    if escolha not in [1, 2]:
        print("Entrada Inválida!")
        print("Tente novamente")


    elif escolha == 1:
        real = float(input("Digite o valor em Reais: R$"))
        retorno = real_para_dolar(real)
        print(f"R${real} equivalem a US${retorno:.2f}")

    elif escolha == 2:
        dolar = float(input("Digite o valor em Dólares: U$"))
        retorno = dolar_para_real(dolar)
        print(f"U${dolar} equivalem a R${retorno:.2f}")


