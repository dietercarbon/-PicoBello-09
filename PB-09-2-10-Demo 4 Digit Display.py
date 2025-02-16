import tm1637
from machine import Pin
from utime import sleep

display = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
 
# Word
display.show("    ")
display.show("AbCd")
sleep(2)
 
#Time with colon
display.numbers(10,40)
sleep(2)
 
#Time with colon
display.number(1040)
sleep(2)

"""
Das vorliegende Python-Programm ist für den Raspberry Pi Pico geschrieben
und verwendet die MicroPython-Plattform. Es steuert ein TM1637-Display,
das eine vierstellige, sieben Segmentanzeige ist. Dieses Display ermöglicht
es, Text und Zahlen darzustellen.

Hier ist eine detaillierte Erläuterung des Programms:

    Import von Modulen:


import tm1637
from machine import Pin
from utime import sleep

    tm1637: Dieses Modul stellt Funktionen zum Steuern des TM1637-Displays bereit.
    machine: Ein Modul, das Funktionen für die Hardwarezugriffe bereitstellt.
    Hier wird die Pin-Klasse verwendet, um die Pins des Raspberry Pi Pico zu steuern.
    utime: Dieses Modul enthält Funktionen für Zeitmessungen. Hier wird sleep verwendet,
    um Pausen im Programmablauf einzufügen.

Initialisierung des Displays:


display = tm1637.TM1637(clk=Pin(0), dio=Pin(1))

Hier wird eine Instanz der TM1637-Klasse erstellt und mit den Pins 0 und 1 verbunden.
Diese Pins werden verwendet, um die Uhrzeitdaten zum Display zu senden.

Anzeige von Text "AbCd":


display.show("    ")
display.show("AbCd")
sleep(2)

Zuerst wird das Display geleert, indem Leerzeichen angezeigt werden. Dann wird der
Text "AbCd" auf dem Display angezeigt. Das Programm wartet dann 2 Sekunden, bevor es fortfährt.

Anzeige von Uhrzeit mit Doppelpunkt:


display.numbers(10, 40)
sleep(2)

Diese Zeile zeigt die Zeit "10:40" auf dem Display an, wobei der Doppelpunkt zwischen
Stunden und Minuten gesetzt wird. Nachdem die Zeit angezeigt wurde, wartet das Programm erneut 2 Sekunden.

Anzeige von Uhrzeit ohne Doppelpunkt:


    display.number(1040)
    sleep(2)

    Hier wird die Uhrzeit "10:40" erneut angezeigt, diesmal jedoch ohne den Doppelpunkt
    zwischen Stunden und Minuten. Das Programm wartet erneut 2 Sekunden, bevor es beendet wird.

Das Programm dient dazu, die verschiedenen Funktionen des TM1637-Displays zu demonstrieren,
einschließlich der Anzeige von Text und Zahlen mit und ohne Doppelpunkt für die Uhrzeit.
Es ermöglicht auch eine kurze Pause zwischen den Anzeigen, um die Lesbarkeit zu verbessern.
"""