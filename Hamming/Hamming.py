# -*- coding: utf-8 -*-
hamming_list = [1,4,11,26,57,120,247] #O número de bits é index + 2 
menssage_size = [3,7,15,31,63,127,255]

def generate_hamming(items_number):
	bits_number = 0		#Número de bits de paridade
	original_info = []
	info = []
	positions_list = []
	for i, v in enumerate(hamming_list):
		if (items_number <= v):
			bits_number = (i + 2)
			break
	if not bits_number == 0:
		for i in range(items_number):	#Receber a informação
			control = 0
			while(control == 0):
				bit_info = int(input("\n>>>>> Digite o número {}: ".format(i + 1)))
				if (bit_info == 0 or bit_info ==1):
					original_info.append(bit_info)
					control = 1
				else:
					print("\n>>>>> O número fornecido não foi binário!")
		info = original_info.copy()
		for i in range(bits_number):	#Preencher a "tabela"
			position = (2 ** i) - 1
			positions_list.append(position)
			info.insert(position, 0)
		for i in range(bits_number):	#Realizar o Cálculo - A ideia é criar uma pilha para fazer a contagem dos "passos" necessários para pular e a flag sinalizar se é para preencher a sequencia ou saltar
			position = positions_list[i]
			info_aux = info[position:len(info)]
			stack = [0 for _ in range(position + 1)]	
			stack_max_limit = len(stack)
			flag = 1	# Se flag = 1 preenche / Se flag = 0 pula
			for j in range(len(info_aux)):
				if(len(stack) == stack_max_limit):
					stack.pop()
					flag = 0
				elif(len(stack) == 0):
					stack.append(0)
					info_aux[j] = 0
					flag = 1
				elif(len(stack) > 0 and len(stack) < stack_max_limit):	#Contagem da Pilha e Preencher os bits na info_aux
					if(flag == 0):
						stack.pop()
					else:
						if info_aux[j] == 1: info_aux[j] = 0
						stack.append(0)
			parity = sum(x for x in info_aux) % 2
			info[position] = parity
		print("\n>>>>> Dados Originais: {}".format(original_info))
		return info
	else: return False

def validate_hamming(items_number):
	info_received = []
	info_original = []
	parity_list = []
	positions_list = []
	wrong_bit_list = []
	bits_number = 0
	for i in range(items_number):
		control = 0
		while(control == 0):
			bit_info = int(input("\n>>>>> Digite o número {}: ".format(i + 1)))
			if (bit_info == 0 or bit_info ==1):
				info_received.append(bit_info)
				control = 1
			else:
				print("\n>>>>> O número fornecido não foi binário!")
	for i, v in enumerate(menssage_size):
		if (len(info_received) <= v):
			bits_number = (i + 2)
			break
	for i in range(bits_number):
		position = (2 ** i) - 1
		positions_list.append(position)
	info_received_aux = info_received.copy()
	for position in positions_list:
		info_received_aux[position] = 0
	for i in range(bits_number):
		position = (2 ** i) - 1
		info_aux = info_received_aux[position:len(info_received_aux)]
		stack = [0 for _ in range(position + 1)]
		stack_max_limit = len(stack)
		flag = 1
		for j in range(len(info_aux)):
			if(len(stack) == stack_max_limit):
				stack.pop()
				flag = 0
			elif(len(stack) == 0):
				stack.append(0)
				info_aux[j] = 0
				flag = 1
			elif(len(stack) > 0 and len(stack) < stack_max_limit):
				if(flag == 0):
					stack.pop()
				else:
					if info_aux[j] == 1: info_aux[j] = 0
					stack.append(0)
		parity = sum(x for x in info_aux) % 2
		parity_list.append(parity)
	for i in range(len(parity_list)):
		if parity_list[i] != info_received[positions_list[i]]:
			wrong_bit_list.append(positions_list[i])
	total = sum((x + 1) for x in wrong_bit_list)
	if not total == 0:
		for i in range(len(info_received)):
			if not (i in positions_list):
				info = info_received[i]
				if not i == total - 1:
					info_original.append(info)
				else:
					if info == 0:
						info_original.append(1)
					else:
			 			info_original.append(0)
		print("\n>>>>> Foi detectado um erro no bit nº {} do grupo: ".format(total))
		print("\n>>>>> {}".format(info_received))
		print("\n>>>>> Grupo de bits finais com o bit corrigido: {}".format(info_original))
	else:
		for i in range(len(info_received)):
			if not (i in positions_list):
				info = info_received[i]
				info_original.append(info)
		print("\n>>>>> Não foi detectado erro.")
		print("\n>>>>> Grupo de bits finais: {}".format(info_original))