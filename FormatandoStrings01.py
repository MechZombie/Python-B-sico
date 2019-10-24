# -*- coding: utf-8 -*-

#Convertendo de string para inteiro
nums = [4,5,6]
msg = "Numbers: {0} {1} {2}".format(nums[0],nums[1],nums[2])
print(msg)


#Ambos exemplos seguem a mesma lógica
print("{0}{1}{0}".format("abra","cad",))

#Outro exemplo
a = "{x},{y},{x}".format(x=5, y=12)
print(a)

