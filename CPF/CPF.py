# -*- coding: utf-8 -*-
import random

def generate_cpf():                                                        
    cpf = [random.randint(0, 9) for x in range(9)]                                                                                                      
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11                                                                  
        cpf.append(11 - val if val > 1 else 0)                                                                                     
    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

def validate_cpf(cpf):
	val_num = cpf[0]
	if not all(val_num == i for i in cpf):
		arr = cpf[0:9]
		val1 = sum((len(arr) + 1 - i) * arr[i] for i in range(9)) % 11
		val1 = 11 - val1 if val1 > 1 else 0
		arr.insert(len(arr),cpf[9])
		val2 = sum((len(arr) + 1 - i) * arr[i] for i in range(10)) % 11
		val2 = 11 - val2 if val2 > 1 else 0
		return True if ((val1 == cpf[9]) and (val2 == cpf[10])) else False
	else:
		return False 
