import random
import json


#pegando os dados de pilotos
def pega_dados():
    with open('formula-e.json') as f:
        dados = json.load(f)
    return dados

dados_formulae = pega_dados()

def nome_piloto(dados, id):
    return dados["pilotos"][str(id)]["nome"]

def nacionalidade_pilotos(nacionalidade):
    pilotos_mesma_nacionalidade = []
    for piloto in dados_formulae["pilotos"]:
        if piloto["nacionalidade"].lower() == nacionalidade.lower():
            pilotos_mesma_nacionalidade.append(piloto)
    return pilotos_mesma_nacionalidade

def mesmo_time(time):
    pilotos_mesmo_time=[]
    for piloto in dados_formulae["pilotos"]:
        if piloto["equipe"].lower() == time.lower():
            pilotos_mesmo_time.append(piloto)
    return pilotos_mesmo_time

#funcão que verifica saldo se possível "abre" um pacote aleatorio e o adicona a sua coleção
def abrir_pacote(jogador, album):
    if jogador["dinheiro"] >= 20:
        pacote = []
        for i in range(3):
            id_piloto_sorteado=random.randrange(1,31)
            piloto_sorteado=nome_piloto(dados_formulae, id_piloto_sorteado)
            pacote.append(piloto_sorteado)
            album.append(piloto_sorteado)
            raridade_piloto=random.randrange(1,4)
            pacote.append(raridade_piloto)
        
        print('Parabens você ganhou:\n'
            f'{pacote[0]} raridade: {pacote[1]}\n'
            f'{pacote[2]} raridade: {pacote[3]}\n'
            f'{pacote[4]} raridade: {pacote[5]}\n')
        
        jogador["dinheiro"]-=20
       
    else:
        print(f'\nSaldo insuficiente {jogador["nome"]}\n')

#recebe do usuario um item que será vendido pela metade do preço de um pacote
def vender_item(album, item_vender):
    while not item_vender in album:
        item_vender=input("Digite um item real:")
    album.remove(item_vender)
    jogador["dinheiro"]+=10
    
def mostrar_colecao(jogador, album):
    print(f'Esta é sua coleção {jogador["nome"]}')
    #itera pelo array printando sua coleção
    for i in range(len(album)):
        print(f'{album[i]}\n')

#Adiciona fundo imaginario ao ususario
def adicionar_fundos(jogador,valor):
    jogador["dinheiro"]+=valor
    print(f"Valor adicionado a carteira ({valor})")

#funcao que verifica inteiro
def num_verificado(msg):
    num = input(msg)
    while not  num.isnumeric():
        num=input(msg)
    num= int(num)
    return num

#boas vindas ao usuario e cadastro de nome e saldo
print("Bem vindo ao E-kids aqui você poderá abrir pacotes para sua coleção vendelos e trocar eles\n")
jogador={
    "nome":"",
    "dinheiro":0
}
jogador["nome"]=(input("Digite seu Nome:\n"))
jogador["dinheiro"]=(num_verificado('Digite o valor do saldo:\n'))
album = []
#menu pricipal com as opções destacadas
while True:
    opcao=num_verificado("Escolha qual opração deseja: \n1-Abrir pacote.\n2-Vender item.\n3-Mostrar Coleção\n4-Adicionar Moedas")

    if opcao == 0:
        break
    elif opcao == 1:                    
        abrir_pacote(jogador, album)
    elif opcao == 2:
        for i in range(len(album)):
            print(f'{album[i]}, ')
        item_vender=input("O nome do item que você deseja vender: ")
        vender_item(album ,item_vender)
    elif opcao == 3:
        mostrar_colecao(jogador, album)        
    elif opcao == 4:
        valor=num_verificado("Digite quanto de saldo deseja adicionar:")
        adicionar_fundos(jogador, valor)       
    else:
        print("Digite uma opcao valida!")
