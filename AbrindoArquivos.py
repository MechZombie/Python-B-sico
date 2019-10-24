# -*- coding: utf-8 -*-

#Abrindo um arquivo com método open()
myfile = open("arquivo.txt")

#É possível passar um segundo parametro "W" = escrita,
# "R" = leitura, esse método pode ser chamado apenas uma vez por arquivo
# "B" = modo binário, "WB" = escrita em binário.

open("arquivo.txt","r")
open("arquivo.txt", "w")
open("arquivo.text", "wb")

#O método close() é usado para fechar o arquivo depois de usado.
myfile.close()

#Escrevendo algum conteúdo em um arquivo.
#Vale ressaltar que abrir um arquivo em modo de escrita, e fechar sem escrever nada
#Deixará o arquivo em branco, pois o modo de escrita sempre sobrescreve o conteúdo 
#Anterior.
file = open("arquivo.txt","w")
file.write("Alguma coisa sendo escrita")
file.close()

#Lendo algum arquivo.
file = open("arquivo.txt","r")
cont = file.read()
print(cont)
file.close()

# file = open("arquivo.txt","r")
# print(file.readlines())




#BOAS PRÁTICAS

#Para evitar desperdícios é interessante que seja usado dentro de um tryCatch

try:
    f = open("arquivo.txt")
    print(f.read())
finally:
    f.close()# Se houver algum erro após a operação de escrita, ainda assim sera salvo seu conteúdo.    


#É comum usar o "WITH", que fechará o arquivo mesmo se houver alguma exception.
#Existe a necessidade de criar uma variável local.
with open("arquivo.txt","w") as f:
    f.write("usando o WITH")

with open("arquivo.txt") as f:
    print(f.read())


#CURIOSIDADE

#Qual o maior número que terá saida no código abaixo?

try:
    print(1)
    assert 2 +2 == 5
except AssertionError:
    print(3) #<-- Essa será a maior saída.
except:
    print(4) # Essa exception só será chamada se a invocação da exception anterior falhar.

  
