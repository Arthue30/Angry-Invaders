import console
import jogoF
import jogoM
import jogoD
from pygame import mixer
import pygame


pygame.init()
pygame.mixer.music.load('marcha-imperial.mp3')
pygame.mixer.music.play(loops=10)
pygame.event.wait()
console.clear()

input("ATENÇÃO ESTE JOGO DEVE SER RODADO EM MODO JANELA TELA CHEIA")
console.clear()

print("                                                                              ANGRY INVADERS")
input("                                                                      Pressione enter para iniciar...")
console.clear()

def dificuldade():
    print("Selecione a dificuldade do jogo:", end='')
    print("\n1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    print("4 - Voltar")
    
def exibirMenu():
    console.clear()    
    print("                                                                              Angry Invaders")
    print("\n\n                                                                                    /\ \n                                                                                   /--\ \n                                                                                  /    \ \n                                                                                 /      \ \n                                                                          ____/ /   /\   \ \____ \n                                                                         /  /  /___----___\  \  \ \n                                                                       /____----          ----____\ \n                                                                 ___----            |||           ----___ \n                                                          ___----                   ||/                  ----___ \n                                                          \____________----H|--_____||_____--|H----____________/ \n                                                                           O+       ||       +O \n                                                                                    () ")
    print("\n\nEscolha uma opção: ", end='')
    print("\n1 - Jogar")
    print("2 - Créditos")
    print("3 - sair")
    
def creditos():
    pygame.mixer.music.pause()
    pygame.mixer.music.load('Star-Wars-tema.mp3')
    pygame.mixer.music.play()
    input("Criadores: \nArthur Sobral de Macêdo \nGabriel Calabrese dos Santos da Silva \nLeonardo de Oliveira Nanes \nSarah Alves da Rocha Vieira ")
    pygame.mixer.music.pause()
    pygame.mixer.music.load('marcha-imperial.mp3')
    pygame.mixer.music.play()
    opcao=0

def jogar():
    J=0
    while (J!=1 and J!=2 and J!=3 and J!=4):
        console.clear()
        dificuldade()
        try:
            J = int(input())
        except:
            J=0
            
    if (J == 1):
        console.clear()
        jogoF.jogar()
    elif (J==2):
        console.clear()
        jogoM.jogar()
    elif (J==3):
        console.clear()
        jogoD.jogar()
    elif (J==4):
        console.clear()
        opcao = 0
        


while True:
    opcao = 0
    while (opcao != 1 and opcao != 2 and opcao != 3):
        console.clear()
        exibirMenu()
        try:
            opcao = int(input())
        except:
            opcao = 0

    if (opcao == 1):
        console.clear()
        jogar()
    elif(opcao ==2):
        console.clear()
        creditos()
    else:
        console.clear()
        input("Volte sempre!")
        exit(0)

