# -*- coding: utf-8 -*-
import CPF

option = 0
control = 0
while option != 3:
	print('''\n		[1] Gerar CPF
		[2] Verificar CPF
		[3] Sair do Programa''')
	option = int(input('\n>>>>> Qual é a sua opção: '))
	if option == 1:
		new_cpf = CPF.generate_cpf()
		print('\n>>>>> Seu novo CPF é: {}'.format(new_cpf))
	elif option == 2:
		strcpf = str(input('\n>>>>> Digita apenas os números do CPF: '))
		if len(strcpf) == 11 and strcpf.isalnum() == True:
			arrcpf = [x for x in strcpf]
			for i in range(11):
				if not any(arrcpf[i] == str(j) for j in range(10)):
					print("\n>>>>> CPF digitado incorretamente")
					control = 1
					break
			if control == 0:
				arrcpf = [int(x) for x in strcpf]
				if CPF.validate_cpf(arrcpf):
					print("\n>>>>> É válido")
				else:
					print("\n>>>>> É inválido")
		else:
			print("\n>>>>> CPF digitado incorretamente")
		control = 0
	elif option == 3:
		print("\n>>>>> Programa Encerrado")
	else:
		print('\n>>>>> Opção Inválida')
	print("<=>" * 30)
