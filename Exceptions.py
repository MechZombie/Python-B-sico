# -*- coding: utf-8 -*-
#Exceptions em python são muito similares à demais linguagens.

try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("Pronto") 
except:
    print("Ocorreu Um erro ")
finally:
    print("Ocorreu um erro inesperado")