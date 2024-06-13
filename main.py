import random
pilotos = ['Nick Cassidy', 'Pascal Wehrlein', 
           'Mitch Evans', 'Oliver Rowland', 
           'Jake Dennis', 'Jean-Éric Vergne', 
           'António Félix da Costa','Maximilian Gunther', 
           'Stoffel Vandoorne', 'Jake Highes',
           'Norman Nato', 'Sam Bird',
           'Sacha Fenestraz', 'Sébastien Buemi',
           'Robin Frijns', 'Nico Muller',
           'Dan ticktum', 'Sérgio Sette Câmara',
           'Jeahan Daruvala', 'Edoardo Mortara',
           'Nyck De Vries', ' Joel Eriksson',
           'Lucas di Grassi', 'Kelvin Van Der Linde',
           'Jordan King', 'Paul Aron' ]


def abrir_pacote(jogador):
    if jogador[1] >= 20:
        piloto_sorteado_1 = random.choice(pilotos)
        raridada_piloto_1 = random.randrange(1,4)
        
        piloto_sorteado_2 = random.choice(pilotos)
        raridada_piloto_2 = random.randrange(1,4)
        
        piloto_sorteado_3 = random.choice(pilotos)    
        raridada_piloto_3 = random.randrange(1,4)
        
        jogador.append(piloto_sorteado_1)
        jogador.append(piloto_sorteado_2)
        jogador.append(piloto_sorteado_3)
        
        print('Parabens você ganhou:\n'
            f'{piloto_sorteado_1} raridade: {raridada_piloto_1}\n'
            f'{piloto_sorteado_2} raridade: {raridada_piloto_2}\n'
            f'{piloto_sorteado_3} raridade: {raridada_piloto_3}\n')
        
        jogador[1]-=20
        print(f'{jogador[1]}')
    else:
        print(f'\nSaldo insuficiente {jogador[1]}\n')
    
def vender_item(item_vender):
    while not item_vender in jogador:
        item_vender=input("Digite um item real:")
    jogador.remove(item_vender)
    jogador[1]+=10
    
def mostrar_colecao():
    print(f'Esta é sua coleção {jogador[0]}')
    for i in range(len(jogador)):
        print(f'{jogador[i]}\n')
    
def adicionar_fundos(valor):
    jogador[1]+=valor
    print(f"Valor adicionado a carteira ({valor})")
    
def num_verificado(msg):
    num = input(msg)
    while not  num.isnumeric():
        num=input(msg)
    num= int(num)
    return num

print("Bem vindo ao E-kids aqui você poderá abrir pacotes para sua coleção vendelos e trocar eles\n")
jogador=[]
jogador.append(input("Digite seu Nome:\n"))
jogador.append(num_verificado('Digite o valor do saldo:\n'))

while True:
    opcao=num_verificado("Escolha qual opração deseja: \n1-Abrir pacote.\n2-Vender item.\n3-Mostrar Coleção\n4-Adicionar Moedas")

    if opcao == 0:
        break
    elif opcao == 1:                    
        abrir_pacote(jogador)
    elif opcao == 2:
        for i in range(len(jogador)):
            print(f'{jogador[i]}, ')
        item_vender=input("O nome do item que você deseja vender: ")
        vender_item(item_vender)
    elif opcao == 3:
        mostrar_colecao()
        print("oi")
    elif opcao == 4:
        valor=num_verificado("Digite quanto de saldo deseja adicionar:")
        adicionar_fundos(valor)       
    else:
        print("Digite uma opcao valida!")
