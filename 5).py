# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

texto = str(input("Digite uma palavra para invertê-la: "))

texto_invertido = texto[::-1]

print(texto_invertido)