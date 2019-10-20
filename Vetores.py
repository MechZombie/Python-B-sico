# -*- coding: utf-8 -*-
#LISTAS

nums = [5,4,3,2,1]
print(nums)

numer = 3
things = ["string",0,[1,2,numer],4.56]
print(things[1])
print(things[1])
print(things[1])

#O indice [2] é um vetor, então passando novamente [2]
#irá retornar a posição [2] do vetor
print(things[2][2])

# irá retornar a letra do indice[6]
str = 'Hello World'
print(str[6])

#Operação 
nums = [7,7,7,7,7]
nums[2] = 5
nums[1] = nums[2]
print(nums)

nums = [1,2,3]
print(nums + [4,5,6]) #[1, 2, 3, 4, 5, 6]
print(nums * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

words = ["spam", "eggs", "sausage"]
print("spam" in words) # subliminarmente é feito uma checagem se "spam" existe em words
print("tomato" in words)

nums = [1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)


#Funções básicas com listas

#Função append add o valor após o ultimo
nums = [1,2,3]
nums.append(4)
print(nums)

#Função len conta quantos items uma lista possui
nums = [1,2,3,4,5]
print(len(nums))

#Função insert, inseri o valor na posição passada, se já estiver ocupada, o valor antigo é passado
#para a posição ao lado
nums = [1,3]
nums.insert(1,2)
nums.insert(3,4)
print(nums)

#Função index, retorna o indice do item passado
letters = ['p','q','r','s']
print(letters.index('r'))# 2

#Função range, cria um vetor de numeros inteiros
numbers = list(range(11))
print(numbers)

nums = list(range(5))
print(nums)

numbers = list(range(3,8)) # cria uma lista com valores de 3 até 7
print(numbers)

numbers = list(range(5,20,2)) # o terceiro argumento é o intervalo
print(numbers)# [5, 7, 9, 11, 13, 15, 17, 19]