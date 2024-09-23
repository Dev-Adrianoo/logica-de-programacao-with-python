"""
  Desenvolva um algoritmo que peça para o usuário informar um número.
  O algoritmo deverá informar se o número é par ou ímpar.

  Inicio: Pedir para o úsuario informar o número
  Processamento: se o resto da divisão do número por 2 for igual a 0, então ele é par
  saida: mostra se o número é par
"""

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Número é par!")
else:
    print("Número digitado é impar!")
