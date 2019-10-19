# -*- coding: utf-8 -*-

#variáveis não podem começar com numeros

a = "2"
b = "2"
print(a+b) # Terá como saida  "22", pois foi feita uma concatenação

a = 2
b = 2
print(a+b) #É realizada uma soma

a = "2"
b = 2
#print(a+b)  Erro, não é possível concatenar nem somar dessa forma.

a = "2"
b = "2"
print(int(a) + int(b)) # Conversão de str para int
print(float(a) + float(b)) # Conversão de str para float

print(int("3" + "4")) #Tem como saida 34 
#pois é feita primeiro a concatenação e depois a converção para inteiro

print(float("210" * int("2"))) # Tem como saida 210210.0
#primeiro o "2" é convertido para int, depois 210 que é uma string é multiplicado
#por 2, então, tudo isso é passado para float.


