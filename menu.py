#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os, sys

"""Menu de lancement des horloges type RTL"""
choix = None

while choix != 1 or choix != 2 or choix != 3:
    for i in range(20):
        print""

    print "MENU HORLOGE \"RTL\""
    print ""
    print "1 -- Horloge avec 2 aiguilles (heures et minutes) plus LED pour seconde"
    print "2 -- Horloge avec 3 aiguilles (heures, minutes et troteuse) LED fixent"
    print "3 -- Horloge sans aiguille affichage avec chiffres \"digitaux\" plus LED pour seconde"
    print "4 -- Sortir"
    print ""
    try:
        choix = int(raw_input("Choix de l'horloge  : 1, 2, 3 ou 4 pour sortir:  "))
    except:
        print "Choisir une horloge 1, 2 ou 3"
        print""
        vide = raw_input("Appuyer sur entrée pour refaire un choix")
        choix = None
        continue
    if choix < 1 or choix > 4:
        print "Choisir une horloge 1, 2, 3 ou 4 pour sortir"
        print""
        vide = raw_input("Appuyer sur entrée pour refaire un choix")
    else:
        if choix == 1:
            os.system("python main.py")
        elif choix == 2:
            os.system("python main2.py")
        elif choix == 3:
            os.system("python main3.py")
        elif choix == 4:
            print choix
            sys.exit(0)
        
        