#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""Version de l'horloge RTL avec 3 aiguilles Heure, minute et seconde les LED du tours sont fixes
avec les LED"""

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

def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

screen=pygame.display.set_mode(( 517, 517), pygame.NOFRAME)
largeur, hauteur = screen.get_size()
screen.fill([0,0,0])

tabLed = cercleLed() #Fabrique des LED

aiguille = pygame.image.load("/home/pi/horlogeRTL/horloge/aiguilleseconde.png").convert_alpha()
rectAiguille = aiguille.get_rect()
rectAiguille = rectAiguille.move(0, 254)

aiguilleMinute = pygame.image.load("/home/pi/horlogeRTL/horloge/aiguille.png").convert_alpha()
rectAiguilleMinute = aiguilleMinute.get_rect()
rectAiguilleMinute = rectAiguilleMinute.move(0, 254)

aiguilleHeure = pygame.image.load("/home/pi/horlogeRTL/horloge/aiguilleH.png").convert_alpha()
rectAiguilleHeure = aiguilleHeure.get_rect()
rectAiguilleHeure = rectAiguilleHeure.move(0, 254)

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
    
    #placement des LED autour sans mouvement. Le mouvement des seconde est fait par une troteuse
    for led in range(61):
        screen.blit(tabLed[led].led,(tabLed[led].rectangle))
    
    #Aiguille des secondes    
    aiguille2, rectAiguille2 = rot_center(aiguille, rectAiguille, 180 - (seconde * 6 + 90))
    screen.blit(aiguille2, rectAiguille2)
    #Aiguille des minutes
    aiguilleMinute2, rectAiguilleMinute2 = rot_center(aiguilleMinute, rectAiguilleMinute, 180 - (minute * 6 + 90) - seconde/12)
    screen.blit(aiguilleMinute2, rectAiguilleMinute2)
    #Aiguille des heures
    aiguilleHeure2, rectAiguilleHeure2 = rot_center(aiguilleHeure, rectAiguilleHeure, 180 - (heure * 30 + 90) - minute * 6 / 12)
    screen.blit(aiguilleHeure2, rectAiguilleHeure2)
    
    pygame.display.flip()
pygame.quit()

