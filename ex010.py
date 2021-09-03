# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M QUADRADOS
h = float(input('Digite a altura em metros: '))
l = float(input('Digite a largura em metro: '))
# area = h*l
# litros = area / 2
print('A área total é {area} e o total de litros necessário para pintar é de {litros} litros de tinta'.format(
    area=h*l, litros=(h*l)/2))
