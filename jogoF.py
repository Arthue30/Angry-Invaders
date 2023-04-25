import console 
from console import *
from time import sleep
from random import randrange
from jconst import *
from calculos import solve1, solve2
from pygame import mixer
import pygame


def jogar():
    
    #historinha
    player=input("Digite o nome do jogador:")
    console.clear()
    input("Há muito tempo , em uma galáxia muito, muito distante...")
    input("A tripulação da Unova estava passando por sérios problemas")
    input("-Capitão {}, nós estamos em apuros...".format(player))
    input("Estamos sendo atacados, são muitos e estão por todos os lados...")
    input("Vamos precisar de sua ajuda!")
    input("\nQUE A FORÇA ESTEJA COM VOCÊ!")

    #define tela
    init(LIMITE_VERT)
    gotoxy(0, 2)
    print('+' * LIMITE, end='', flush=True)
    gotoxy(0, LIMITE_VERT  )
    print('-' * LIMITE, end='', flush=True)
    gotoxy((LIMITE / 2) - 13, 0)
    print("Destrua as naves inimigas!", end='') 
    gotoxy((LIMITE/2)-10,LIMITE_VERT)
    print("Naves destruidas:0 /10", end='') 
    gotoxy((LIMITE/2)-3,LIMITE_VERT-1)
    print("Vidas: 10",end='')

   
    #Cria as balas
    balas = [   {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
                {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} }]
    for i in range(0, len(balas)):
        balas[i]["ativa"] = False

    #cria as naves
    naves = [  { "img":"<╬", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"<╬", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"<╬", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"(>", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"(>", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"<╬", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"<╬", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"<╬", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"(>", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"(>", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"(>", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"(>", "x":LIMITE, "y":LIMITE_VERT, "ativa": False, "traj": {"A":0, "B": 0, "C": 0} }]
    for j in range(0, len(naves)):
            naves[j]["ativo"] = False

    '''
    cometas = [ { "img":"*", "x":LIMITE, "y":LIMITE_VERT, "ativo": False, "traj": {"A":0, "B": 0} },
                { "img":"☼", "x":LIMITE, "y":LIMITE_VERT, "ativo": False, "traj": {"A":0, "B": 0} },
                { "img":"*", "x":LIMITE, "y":LIMITE_VERT, "ativo": False, "traj": {"A":0, "B": 0} },
                { "img":"☼", "x":LIMITE, "y":LIMITE_VERT, "ativo": False, "traj": {"A":0, "B": 0} },
                { "img":"☼", "x":LIMITE, "y":LIMITE_VERT, "ativo": False, "traj": {"A":0, "B": 0} },
                { "img":"*", "x":LIMITE, "y":LIMITE_VERT, "ativo": False, "traj": {"A":0, "B": 0} }]'''

    kills = 0
    Vidas = int(10)
    coefAng = 1
    intervalo = 15   

    while True:
        #Lançar nave
        if (randrange(15) % len(naves) == 0 and intervalo < 0):
            intervalo = len(naves) + randrange(10)
            j = 0
            for nave in naves:
                if (not nave["ativa"]):
                    nave["ativa"] = True
                    nave["x"] = LIMITE
                    nave["y"] = LIMITE_VERT/2 + randrange(20)
                    nave["traj"]["C"] = nave["y"]
                    nave["traj"]["A"] = (max(-15, 4 - nave["traj"]["C"])) / ((LIMITE/2) * (LIMITE/2 - LIMITE)) # 2 = y min
                    nave["traj"]["B"] = - nave["traj"]["A"] * LIMITE
                    break
                j += 1

        #apaga, move e desenha naves
        j = 0
        for nave in naves:
            # Apaga o nave
            gotoxy(nave["x"], nave["y"])
            print("  ", end='')


            #Muda as posições da nave 
            if nave["ativa"]:
                nave["x"] -= 1    
                nave["y"] = int(solve2(nave["traj"]["A"], nave["traj"]["B"], nave["traj"]["C"], nave["x"]))

                #faz a nave refazer trajeto
                if nave["x"] <= 0 :
                   nave["ativa"] = False

                #desenha nave
                else:
                    gotoxy(nave["x"], nave["y"])
                    print(nave["img"], end='') 
            j += 1

        #COMANDOS DO USUÁRIO
        if (kbhit()):
            c = hitKey()
            
            #Atirar bala
            if (ord(c) == ord(' ')):
                for bala in balas:
                    if (not bala["ativa"]):
                        bala["ativa"] = True
                        bala["x"] = 8
                        bala["y"] = (LIMITE_VERT/2)
                        bala["traj"]["A"] = coefAng 
                        bala["traj"]["B"] = -bala["traj"]["A"] * LIMITE 
                        bala["traj"]["C"] = bala["y"]
                        break

            if (ord(c) == ord('s') or ord(c) == ord('S')):
                coefAng = (max(-10,7-bala["traj"]["C"])) / ((LIMITE/2) * (LIMITE/2 - LIMITE))
            if (ord(c) == ord('w') or ord(c) == ord('W')):
                coefAng = -(max(-15,8-bala["traj"]["C"])) / ((LIMITE/2) * (LIMITE/2 - LIMITE))
                
                        
        #apaga, move e desenha balas
        
        for bala in balas:
            if (bala["ativa"]):
                gotoxy(bala["x"], bala["y"])
                print(' ', end='')

                bala["x"] += 1   #FAZER x da Bala se mover pelo coefAng bala["y"]  #()
                bala["y"] = int(solve2(bala["traj"]["A"],bala["traj"]["B"],bala["traj"]["C"],bala["x"]))
                if (bala ["x"] >= LIMITE or bala["y"] >=LIMITE_VERT or bala["y"] <= 3):
                    bala["ativa"] = False
                else:
                    gotoxy(bala["x"], bala["y"])
                    print('•',end='')

        #desenha canhão:
        gotoxy(4,(LIMITE_VERT/2)-2)
        print('  <|\ \n     {| )\n     <|/', flush=True)

        #desenha estrelas
        gotoxy(80,7)
        print("☼", end='', flush=True)
        gotoxy(55,6)
        print("*", end='',flush=True)
        gotoxy(100,22)
        print("*", end='',flush=True)
        gotoxy(17,18)
        print("☼", end='',flush=True)
        gotoxy(LIMITE-10,20)
        print("☼", end='',flush=True)
        gotoxy(13,35)
        print("*", end='',flush=True)
        gotoxy(20,40)
        print("*", end='',flush=True)
        gotoxy(28,27)
        print("*", end='',flush=True)
        gotoxy((LIMITE/2) -10,LIMITE_VERT/2)
        print("☼", end='',flush=True)
        gotoxy(LIMITE-10,LIMITE_VERT-10)
        print("*", end='',flush=True)
        gotoxy(77,23)
        print("*", end='',flush=True)
        gotoxy(30,7)
        print("*", end='',flush=True)
        gotoxy(LIMITE/2-2,LIMITE_VERT-10)
        print("*", end='',flush=True)
        gotoxy((LIMITE/2)+3,LIMITE_VERT-11)
        print("*", end='',flush=True)
        gotoxy((LIMITE/2)+2,LIMITE_VERT-8)
        print("*", end='',flush=True)
        gotoxy(LIMITE-30,8)
        print("☼", end='',flush=True)
        gotoxy(LIMITE-55,16)
        print("☼", end='',flush=True)
        gotoxy(LIMITE-50,LIMITE_VERT-20)
        print("*", end='',flush=True)
        gotoxy(LIMITE, LIMITE_VERT)
        print('-' * LIMITE, end='', flush=True)

        #pontuações de acerto
        acertou = 0
        for bala in balas:
            for nave in naves:
                if (bala["ativa"] and nave["ativa"]
                        and bala["x"] == nave["x"]
                        and bala["y"] == nave["y"]):
                    acertou = True
                    nave["ativa"] = False
                    bala["ativa"] = False
                    break

        #pontuações de deixar nave passar
        vacilou = 0
        for nave in naves:
            if (nave["ativa"]
                and nave ["x"] == 1):
                vacilou = True
                break

        #sobre pontuação
        if (acertou):
            kills += PONTOS_ACERTO
            gotoxy((LIMITE/2)+7, LIMITE_VERT)
            print(kills, end='')

        #tira vida
        if (vacilou):
            Vidas += PONTOS_ERRO
            gotoxy((LIMITE/2)+3,LIMITE_VERT-1)
            print(' ',Vidas, end='')



        win = lambda : kills >= 10
        if (win()):
            console.clear()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Star-Wars-tema.mp3')
            pygame.mixer.music.play()
            gotoxy((LIMITE/2)-4, LIMITE_VERT/ 2)
            input("YOU WIN!")
            pygame.mixer.music.stop()
            pygame.mixer.music.load('marcha-imperial.mp3')
            pygame.mixer.music.play(loops=10)
            break
        
        gameOver = lambda : Vidas <= 0
        if (gameOver()):
            console.clear()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('efeitos-sonoros-ratinho.mp3')
            pygame.mixer.music.play(loops=5)
            gotoxy((LIMITE/2) -5, LIMITE_VERT / 2)
            input("GAME OVER!")
            pygame.mixer.music.stop()
            pygame.mixer.music.load('marcha-imperial.mp3')
            pygame.mixer.music.play(loops=10)
            break

        print(end='',flush=True)
        sleep (0.05)
        intervalo -= 1


