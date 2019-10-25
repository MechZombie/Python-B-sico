# -*- coding: utf-8 -*-

#Também conhecidas como funções anonimas,semelhantes as arrows functions do JS

################################################
#Lambda
print((lambda x: x**2 +5*x+4) (-4))

#Named function
def polynomial(x):
    return x**2 +5*x+4

print(polynomial(-4))

#################################################

#Funções lambdas podem ser salvas em uma Variáve

double = lambda x: x*2
print(double(7))

#Qual o resultado desse código

triple = lambda x: x*3
add = lambda x,y: x+y
print(add(triple(3),4))