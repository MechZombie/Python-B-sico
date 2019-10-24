# -*- coding: utf-8 -*-

#Dictionaries
#Sua sintaxe é muito semelhante ao formato JSON

ages = {"Dave":24,"Mary":20}
print(ages["Dave"])
print(ages["Mary"])

cars = {"BMW":"blue","VOLVO":"red","False":"funciona"}
print(cars["BMW"])

#Funções comuns 
squares = {1:1,2:4,3:"error",4:16}
squares[8] = 64
squares[3] = 9
print(squares)

pairs = {1:"apple",
"orange":[2,3,4],None:"True"}

print(pairs.get("orange"))

#É possível checar se um determinado dado existe dentro do Dictionarie.
nums = {
    1:"one",
    2:"two",
    3:"three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

#Curiosidade
fib = {1:1,2:1,3:2,4:3}
print(fib.get(4,0) + fib.get(7,5))# o segundo parametro passado, é um tipo de padrao,
#caso não exista o valor, o compilador vai usar o valor passado como padrão.
