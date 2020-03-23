#======================================================================================================================================================#
#Dieses Programm dient der Überwachung von CPU und RAM-Auslastung, sowie freiem Speicherplatz.                                                         #
#Es schickt in einem Interval eine E-Mail mit dem Log der aktuellen Auslastugen im Anhang, wenn ein kritischer Wert überschritten wurde.               #
#Außerdem kann man sich eine Übersicht über die Systemwerte ausgeben lassen. zudem ngibt es eine Hilfe Option.                                         #
#======================================================================================================================================================#

import MainLog, threading
from SystemInfo import systemwerte
from pynput.keyboard import Key, Listener
from getpass import getuser


program_run = True


#Mit dieser Methode wird entweder der Log gestartet, Systeminformationen ausgegeben oder die Hilfe geöffnet,
#jenachdem was man in  die Eingabe eintippt. Die Eingabe ist nicht "CapSensitiv".
#Sie läuft in einem Thread und wird durch ändern des Boolean "program_run" auf False oder True gestoppt oder gestartet.
def programstart():
    global program_run
    print('Hallo ' + getuser() + '\n'
          + 'Dieses Programm kann entweder deine Systemwerte in einem Log anzeigen,'
          + '\nsowie in einer Datei speichern, oder die Systeminfo deines PCs anzeigen.'
          + '\nMit der ESC-Taste lässt sich der Log unterbrechen und du springst zurück in die Eingabe.'
          + '\nMit der Leertaste lässt sich das Programm beenden.'
          )
    while ~program_run:
        log = input('Schreibe einfach Log für den Log, oder Systeminfo für eine übersicht deiner Systeminformationen.' +
                    'Oder H für Hilfe.' +
                    '\nEingabe: ')
        if log.lower() == 'log':
            program_run = True
            start_mainlog()
        elif log.lower() == 'systeminfo':
            program_run = False
            systemwerte()
        elif log.lower() == 'h':
            print("\nBitte wenden Sie sich an ihren Systemadministrator wenn Sie weitere Hilfe benötigen!!!"
                  + "\n")
        else:
            print('\nDie Eingabe war ungültig. Haben Sie sich verschrieben?')

#Hier werden alle Methoden für das Logging in einer Schleife ausgeführt.
def start_mainlog():
    while program_run:
        MainLog.cpu()
        MainLog.ram()
        MainLog.ssd()

#Prüft ob die "Leertaste" gedrückt wurde
def taste_druecken(key):
    check_key(key)

#Wenn die "Leertaste" gedrückt wird, wird das Programm beendet.
def taste_loslassen(key):
    if key == Key.space:
        return False

#Wenn die Taste "ESC" gedrückt wird, wird der Boolean auf FALSE gesetzt wodurch die Methode "programstart" erneut ausgeführt wird.
def check_key(key):
    global program_run
    if key in [Key.esc]:
        program_run = False

#Erstellt einen Thread namens thread1 und führt in diesem Thread die Methode programstart aus.
thread1 = threading.Thread(target=programstart)
#Daemon wird benötigt, damit man den thread1 auch beenden kann.
thread1.daemon = True
#Startet den thread1
thread1.start()
#Führt die Methoden "taste_druecken" und "taste_loslassen" zu "listener" zusammen.
with Listener(on_press=taste_druecken, on_release=taste_loslassen) as listener:
    listener.join()
