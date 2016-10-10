#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""Version de l'horloge RTL sans aiguille avec les secondes qui s'allume
avec les LED et l'heure digitale au centre"""

#placement de l'horloge sur la fenetre de l'OS
x = 520 
y = 0 
import  os 
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame
from pygame.locals import *
import numpy
import time
from ledHorloge import *
from datetime import datetime

screen=pygame.display.set_mode(( 517, 517), pygame.NOFRAME)
largeur, hauteur = screen.get_size()
screen.fill([0,0,0])

tabLed = cercleLed() #Fabrique des lED

chiffre = [] #Les chiffre dans un tableau
for i in range(10):
    chiffre.append(pygame.image.load("/home/pi/horlogeRTL/horloge/" + str(i) + ".png").convert_alpha())

#LED du centre
ledCentre = pygame.image.load("/home/pi/horlogeRTL/horloge/Led5.png").convert_alpha()

running=True
while running:
    for event in pygame.event.get(): 
        if event.type == KEYDOWN:
            running=False
            
    screen.fill([0,0,0])
    
    maintenant = datetime.now()
    seconde = maintenant.second 
    minute = maintenant.minute     
    heure = maintenant.hour
    
    #Mouvement des LED au tour toutes les secondes
    if seconde == 0:
        screen.blit(tabLed[60].led,(tabLed[60].rectangle))
    else:
        for led in range(seconde):
            led = led + 1
            screen.blit(tabLed[led].led,(tabLed[led].rectangle))
            
    #Affichage des heures si moins de 10 heures affichage d'un chiffre
    if heure < 10:
        screen.blit(chiffre[heure],(170, 193))
    else:
        heure = str(heure)
        screen.blit(chiffre[int(heure[0])],(90, 193)) 
        screen.blit(chiffre[int(heure[1])],(170, 193))
        
    #Affichage des minutes si moins de 10 minutes affichage avec un 0 devant
    if minute < 10:
        screen.blit(chiffre[0],(270, 193))
        screen.blit(chiffre[minute],(350, 193))
    else:
        minute = str(minute)
        screen.blit(chiffre[int(minute[0])],(270, 193))
        screen.blit(chiffre[int(minute[1])],(350, 193))
    
    #Clignotemenet des deux points
    if seconde%2 == 0:
        screen.blit(ledCentre,(245, 220))
        screen.blit(ledCentre,(245, 280))
    
    pygame.display.flip()
pygame.quit()

