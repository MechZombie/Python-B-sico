# -*- coding: utf-8 -*-

val = [0,1,2,3,4,5,6,7,8,9]
print(min(val))
print(max(val))
print(sum(val))#Realiza a soma de todos os valores do vetor

#Acertei de primeira
#Qual a saída desse código

a = min([sum([11,22]), max(abs(-30),2)])
print(a)#A saída é 30!!


#É esse método tem uma forma de leitura quase que humana

nums = [55,44,33,22,11]
#Se todos os valores de "i" forem maior que "5", para "i" sendo cada indice de "nums"
if all([i>5 for i in nums]):
    print("Todos são maiores que 5")


if any([i%2 == 0for i in nums]):
    print("Existe números pares")


for v in enumerate(nums):
    print(v)    


#Contando quantas vezes uma determinada letra aparece num texto
#Declarando a função

def count_char(text,char):
    count = 0
    for c in text:
        if c == char:
            count+= 1
    return count            

filename = input("digite")
with open(filename) as f:
    text = f.read()

print(count_char(text,"a"))    