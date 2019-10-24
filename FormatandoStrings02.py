# -*- coding: utf-8 -*-
#Funções comuns


texto = "Hello Me"
#Não sei o motivo, mais o replace não funciona se a alteração for feita antes do print
texto.replace("Me","World")
print(texto.replace("Me","World"))#Funciona apenas se for feita dentro do print
print(texto.startswith("Hello"))
print(texto.upper())
print(texto.lower())
print(texto.split())#Retorna um vetor
