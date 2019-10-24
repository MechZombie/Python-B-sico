# -*- coding: utf-8 -*-

#Basicamente é uma forma de tirar pedaços de um vetor.

squares = [0,1,2,3,4,5,6]
print(squares[2:6])# Tem como saída os valores da posição 2 até 5
print(squares[0:2])

#Se o indice inicial for omitido, terá o primeiro indice como padrão
print(squares[:3])

#Se o indice final for omitido, terá o ultimo indice como padrão.
print(squares[0:])

#É possível passar um terceiro parametro, que será uma alternancia entre valores.
print(squares[::2])#Terá como saida toda a lista, pulando de 2 em 2.
print(squares[0:5:4])

#Valores negativos em uma lista, seram entendidos como valores finais da lista
print(squares[1:-1])
print(squares[-1:0])#Não consegui entender muito bem o por que dessa saida '[]'
print(squares[0:5:-1])#Ésse aqui também


#Comprehensions list
#É uma forma de manipular listas aplicando uma expressão para elas.
#Em outras palavras será aplicado a multiplicação por 2 em cada indice do vetor criado de 0 a 9

even = [i*2 for i in range(10)]
print(even)
even1 = [i+10 for i in range(10)]
print(even1)

#É possível passar um if junto

event2 = [i*2 for i in range(10) if i*2 % 2 ==0]
print(event2)

#Tentar criar listas muito enormes iram resultar em "MemoryError"
#even = [2*i for i in range(10**100)]