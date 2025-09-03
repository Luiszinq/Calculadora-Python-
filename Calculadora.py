import runpy
import string
from dataclasses import replace
import sys,subprocess
import os
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

print("Bem Vindo A Calculadora!")
print("Digite 1 para Adição")
print("Digite 2 para Subtração")
print("Digite 3 para Divisão")
print("Digite 4 para Multiplicação")
print("Digite 5 para Sair")
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
elif calcesc == "5":
    print("Você escolheu, sair do programa!, tchau!")
    exit(None)
else:
    print("Opção Invalida! Tente novamente!")
    runpy.run_module("Calculadora.py")
escolha = input("Desejas resetar o programa? S para Sim e qualquer outra tecla para não!")
if escolha == "S":
    limpar_terminal()
    runpy.run_path('Calculadora.py')
else:
    print("Obrigado por usar a Calculadora")