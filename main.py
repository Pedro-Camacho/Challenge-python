import random
jogador = ['Jogador do Momento', 100]

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
           'Nyck De Vries', ' Joel, Eriksson',
           'Lucas di Grassi', 'Kelvin Van Der Linde',
           'Jordan King', 'Paul Aron' ]


def abrir_pacote():
    piloto_sorteado_1 = random.choice(pilotos)
    raridada_piloto_1 = random.randrange(0,3)
    
    piloto_sorteado_2 = random.choice(pilotos)
    raridada_piloto_2 = random.randrange(0,3)
    
    piloto_sorteado_3 = random.choice(pilotos)    
    raridada_piloto_3 = random.randrange(0,3)
    
    jogador.append(piloto_sorteado_1)
    jogador.append(piloto_sorteado_2)
    jogador.append(piloto_sorteado_3)
    
    print('Parabens você ganhou:\n'
          f'{piloto_sorteado_1} raridade: {raridada_piloto_1}\n'
          f'{piloto_sorteado_2} raridade: {raridada_piloto_2}\n'
          f'{piloto_sorteado_3} raridade: {raridada_piloto_3}\n')
    
def vender_item(item_vender):
    jogador[item_vender].pop
    print(jogador)
    
def mostrar_colecao():
    for i in range(len(jogador)):
        print(f'{jogador[i]}\n')
    
    
    
print("Bem vindo ao E-kids aqui você poderá abrir pacotes para sua coleção vendelos e trocar eles")

while True:
    opcao=input("Escolha qual opração deseja: \n1-Abrir pacote.\n2-Vender item.\n3-\n4-Mostrar Coleção\n 5- Adicionar Moedas")
    while not opcao.isnumeric():
        opcao=input("Escolha qual opração deseja: \n1-Abrir pacote.\n2-Vender item.\n3-Mostrar Coleção\n 4- Adicionar Moedas")
    opcao=int(opcao)

    if opcao == 0:
        break
    elif opcao == 1:
        abrir_pacote()
        if jogador[2]>20:
            abrir_pacote()
            jogador[2]-20
        else:
            print("Saldo insuficiente")
    elif opcao == 2:
        item_vender=input("O nome do item que você deseja vender")
        vender_item(item_vender)
    elif opcao == 3:
        mostrar_colecao()
        print("oi")
    elif opcao == 4:
        #adicionar_fundos()
        print("oi")
    else:
        
        print("Digite uma opcao valida!")
