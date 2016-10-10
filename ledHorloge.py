#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from math import *

class ledHorloge():
    """Fabrique une LED Verte ou Rouge pour le tour de l'horloge Chaque LED à une couleur 
    et une postion"""
    def __init__(self, x, y, color): 
        ledVerte = pygame.image.load("/home/pi/horlogeRTL/horloge/Led5.png").convert_alpha()
        ledRouge = pygame.image.load("/home/pi/horlogeRTL/horloge/Led5R.png").convert_alpha()
        self.rectangle = ledRouge.get_rect()
        if color == "V":
            self.led = ledVerte
        else :
            self.led = ledRouge
        self.rectangle = self.rectangle.move(x, y)
        
"""Fonction qui faquique les LED pour le tour de l'horloge
Les les sont vertes sauf toutes les 5 une LED rouge"""       
def cercleLed():
    leds = []
    for i in range(61):
        if i in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60):
            color = "R"
        else:
            color = "V"
        i = i - 15
        #la postion X, Y sur le cercle 
        X = int(round(250 + 250*cos(i*pi/30), 0));
        Y = int(round(250 + 250*sin(i*pi/30), 0));
        leds.append(ledHorloge(X,Y,color))
    return leds
    
    
    
    
    