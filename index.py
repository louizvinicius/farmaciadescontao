print("\n\tFARMACIA DESCONTÃO")
print("Confira seu aumento de salario")

salario = float(input("Digite seu salario: R$ "))

if salario <= 280.00:
    porcentagem = (salario / 100) * 20 + salario
    print(f"\n**********\nSeu antigo salario: R$ {salario}\nA porcentagem é de: 20%\n"
          f"Aumentou R$ {(porcentagem-salario)}\n Seu novo salario: R$ {porcentagem}\n**********")

if (salario >= 280.01) and (salario <= 700.00):
    porcentagem = (salario / 100) * 15 + salario
    print(f"\n**********\nSeu antigo salario: R$ {salario}\nAumento de: 15%\n"
          f"Aumentou R$ {(porcentagem-salario)}\nSeu novo salario: R$ {porcentagem}\n**********")

if (salario >= 700.01) and (salario <= 1500.00):
    porcentagem = (salario / 100) * 10 + salario
    print(f"\n**********\nSeu antigo salario: R$ {salario}\nAumento de: 10%\n"
          f"Aumentou R$ {(porcentagem-salario)}\nSeu novo salario: R$ {porcentagem}\n**********")

if salario >= 1500.01:
    porcentagem = (salario / 100) * 5 + salario
    print(f"\n**********\nSeu antigo salario: R$ {salario}\nAumento de: 5%\n"
          f"Aumentou R$ {(porcentagem-salario)}\nSeu novo salario: R$ {porcentagem}\n**********")