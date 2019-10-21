import Hamming

option = 0
control = 0
while option != 3:
	print('''\n		[1] Enviar um grupo de bits
		[2] Verificar um grupo de bits recebido
		[3] Sair do Programa''')
	option = int(input('\n>>>>> Qual é a sua opção: '))
	if option == 1:
		items_number = int(input("\n>>>>> Digite a quantidade de bits do grupo original: "))
		info = Hamming.generate_hamming(items_number)
		if info: 
			print('\n>>>>> Dados que serão enviados: {}'.format(info)) 
		else: print('\n>>>>> Erro - Excedeu o limite da informação')
	elif option == 2:
		items_number = int(input("\n>>>>> Digite a quantidade de bits que foram recebidos: "))
		Hamming.validate_hamming(items_number)
	elif option == 3:
		print("\n>>>>> Programa Encerrado")
	else:
		print('\n>>>>> Opção Inválida')
	print("<=>" * 30)