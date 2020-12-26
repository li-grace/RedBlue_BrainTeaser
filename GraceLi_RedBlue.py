""" Red OR Blue Game | Grace Li
Instructions: click on the word reading the color of the top box.
For example, if you are given the word BLUE in the colour RED,
click on the bottom box that says the colour RED.
the player has 10s to answer each question or lose a point.
"""
import pygame #import and initialize necessary values
from random import randint
pygame.init()
done,clock = False,pygame.time.Clock()
window = pygame.display.set_mode((500,400)) #set up basic display and background
pygame.display.set_caption("Red or Blue?")

#create lists of important variables
font = pygame.font.Font(None, 55)
red_red = font.render("RED", True, (255,0,0))
red_blue = font.render("RED", True, (0,0,255))
blue_red = font.render("BLUE", True, (255,0,0))
blue_blue = font.render("BLUE", True, (0,0,255))
qtextList = [red_red,red_blue,blue_red,blue_blue]
genNewQ = True

curIndex, timer, score = 0, 0, 0
a1, a2, a1st = 0, 0, 0
mouseX, mouseY = 0, 0
ansList = [(0,1),(2,3),(0,1),(2,3)]
time_text = font.render("%.2f" %((600-timer)/60), True, (200,200,200))
wrongAnsc = 0

while not done:
    for event in pygame.event.get(): #set up x button for window closing
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseX, mouseY = pygame.mouse.get_pos()

    window.fill((255,255,255))

    if wrongAnsc > 0 and wrongAnsc < 15:
        wrongAnsc += 1
        window.fill((200,0,0))
        if wrongAnsc == 15:
            wrongAnsc = 0
        
    pygame.draw.rect(window,(220,220,220),(180,50,120,60)) #top box
    pygame.draw.rect(window,(220,220,220),(90,240,120,60)) #box 1
    pygame.draw.rect(window,(220,220,220),(280,240,120,60)) #box 2
    
    if genNewQ: 
        curIndex,a1,a2 = randint(0,3),randint(0,1),a1+2
        while a1 + 2 == a2:
            a2 = randint(2,3)
        a1st = randint(0,1)
        genNewQ = False
        
    window.blit(qtextList[curIndex], (190,65))
    if a1st:
        window.blit(qtextList[a1], (100,250))
        window.blit(qtextList[a2], (290,250))
        b1,b2 = a1,a2
    else:
        window.blit(qtextList[a2], (100,250))
        window.blit(qtextList[a1], (290,250))
        b1,b2 = a2,a1

    if mouseX != 0 and mouseY != 0:
        if mouseY >= 240 and mouseY <= 300:
            if mouseX >= 90 and mouseX <= 210:
                if b1 in ansList[curIndex]:
                    score += 1
                    genNewQ,timer = True,0
                else:
                    score -= 1
                    genNewQ,timer,wrongAnsc = True,0,1
            elif mouseX >= 280 and mouseX <= 400:
                if b2 in ansList[curIndex]:
                    score += 1
                    genNewQ,timer = True,0
                else:
                    score -= 1
                    genNewQ,timer,wrongAnsc = True,0,1                   
        mouseX, mouseY = 0, 0

    timer += 1
    if timer > 600: #60 x 10s
        timer,genNewQ = 0, True
        score -= 1
        
    score_text = font.render(str(score), True, (100,100,100))
    window.blit(score_text, (10,10))

    if timer%10 == 0:
        time_text = font.render("%.2f" %((600-timer)/60), True, (200,200,200))
    window.blit(time_text, (400,10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
