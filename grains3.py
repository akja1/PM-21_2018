# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:58:52 2018

@author: Alina
"""

"""
Created on Sun May  6 20:09:50 2018

@author: Alina
"""

def get_square_number(benutzereingabe):
    while True:
        squares_number = 0
        try:
           squares_number = int(benutzereingabe)
           return squares_number
        except:
            benutzereingabe = input("Vorherige Eingabe war keine Zahl! Geben Sie eine Zahl ein:\n")
            continue

def validate_square_number(squares_number):
    while True:
       # valid_squares_number = 0
       if squares_number < 1 or squares_number > 64:
           benutzereingabe = input("Zahl nicht zwischen 1 und 64! Wählen Sie eine Zahl zwischen 1 und 64:\n")
           squares_number = get_square_number(benutzereingabe)
           continue
       return squares_number

def on_square(squares_number):
    rice_on_one_square = 2**(squares_number-1)
    return rice_on_one_square
    
def total_after(squares_number):
    sum_on_square = 0
    for index in range(1, squares_number + 1):
        sum_on_square += on_square(index)
    return sum_on_square


 #hier startet das Hauptprogramm
benutzereingabe = input("Von welchem Quadrat des Schachbretts soll die Anzahl der Reiskörner ermittelt werden?\n")

squares_number = get_square_number(benutzereingabe)

squares_number = validate_square_number(squares_number)

rice_on_one_square = on_square(squares_number)

sum_of_squares = total_after(squares_number)

if squares_number == 1:
    print("Für das 1. Feld erhält der Mann 1 Korn Reis als Belohnung")
else:
    print("Für das " + str(squares_number) + ". Feld erhält der Mann " + str(rice_on_one_square) + " Körner Reis als Belohnung.")
    print("Für die Felder 1 bis " + str(squares_number)  + " erhält der Mann " + str(sum_of_squares) + " Reiskörner.")

