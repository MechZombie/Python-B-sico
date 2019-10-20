# -*- coding: utf-8 -*-

#os metodos usam identação ao inves de {}

#IF
if 10 > 5:
       print("10 é maior 5")
else:
       print("10 é menor que 5")       

print("Fim do programa")




#WHILE
i = 1
while i <= 5:
       print(i)
       i += 1
print("terminado")       

#FOR LOOP
words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")
# Ambos códigos fazem a mesma coisa ============================+
words = ["hello", "world", "spam", "eggs"]                      
counter = 0
max_index = len(words) - 1

while counter <= max_index:
       word = words[counter]
   print(word + "!")
   counter = counter + 1  
#==============================================================+