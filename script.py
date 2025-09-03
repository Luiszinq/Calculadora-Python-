import runpy

print("Bem Vindo A Calculadora!")
print("Digite 1 para Adição")
print("Digite 2 para Subtração")
print("Digite 3 para Divisão")
print("Digite 4 para Multiplicação")
calcesc = input("Digite Aqui!:")
if calcesc == "1":
    print("Você escolheu a Adição, digite um número!")
    ns1 = int(input("Digite Aqui:"))
    print("Agora, Digite um segundo!")
    ns2 = int(input("Digite Aqui:"))
    print("O resultado é:", ns1 + ns2)
elif calcesc == "2":
    print("Você escolheu a Subtração, Digite um número!")
    nss1 = int(input("Digite Aqui:"))
    print("Agora, Digite um segundo!")
    nss2 = int(input("Digite Aqui:"))
    print("O resultado é:", nss1 - nss2)
elif calcesc == "3":
    print("Você escolheu a Divisão, Digite um número!")
    nd1 = int(input("Digite Aqui:"))
    print("Agora, Digite um segundo!")
    nd2 = int(input("Digite Aqui:"))
    print("O resultado é:",nd1 / nd2)
elif calcesc == "4":
    print("Você escolheu a Multiplicação, Digite um número!")
    nm1 = int(input("Digite Aqui:"))
    print("Agora, Digite um segundo!")
    nm2 = int(input("Digite Aqui:"))
    print("O resultado é:", nm1 * nm2)
escolha = input("Desejas resetar o programa? S para Sim e qualquer outra tecla para não!")
if escolha == "S":
    runpy.run_path('script.py')
else:
    print("Tchau e obrigado por usar a calculadora!")