# -*- coding: utf-8 -*-

#Programação Funcional
''' A idéia principal por trás da programação funcional, são as famosas "higher-order
functions", que são funções que recebem outras funções como parametros.'''

def apply_twice(func,arg):
    return func(func(arg))

def add_five(x):
    return x+5

print(apply_twice(add_five,10))

##Não entendi nada desse código!
def test(func, arg):
      return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))

'''Programação funcional trás o conceito de funções puras, que são aquelas não tem efeitos
colaterais e retornam um valor que depende apenas de seus argumentos.'''

def pure_function(x):
    y = x**2
    z = x+y
    return z

print(pure_function(5))    