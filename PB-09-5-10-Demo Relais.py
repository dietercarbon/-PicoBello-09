# Bibliotheken laden
from machine import Pin
from time import sleep

# Initialisierung von GPIO14 als Ausgang
device = Pin(5, Pin.OUT, value=0)

# LED einschalten
print('EIN')
device.on()

# 3 Sekunden warten
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)

# LED ausschalten
print('AUS')
device.off()

"""
Das vorliegende MicroPython-Programm ist für den Raspberry Pi Pico geschrieben
und dient dazu, ein Relais über einen GPIO-Pin ein- und auszuschalten.
Hier ist eine detaillierte Erläuterung:

    Import von Modulen und Initialisierung:

from machine import Pin
from time import sleep

    machine: Ein Modul, das Funktionen für Hardwarezugriffe bereitstellt.
    Hier wird die Pin-Klasse verwendet.
    time: Ein Modul zur Zeitmessung. Die Funktion sleep wird verwendet,
    um Pausen im Programmablauf einzufügen.

Initialisierung des GPIO-Pins als Ausgang:

device = Pin(5, Pin.OUT, value=0)

Hier wird der Pin mit der Nummer 5 als Ausgang initialisiert. Der
Parameter value=0 setzt den Anfangszustand des Pins auf 0 (ausgeschaltet).

Einschalten des Relais:

print('EIN')
device.on()

Dieser Abschnitt des Codes schaltet das Relais ein, indem der GPIO-Pin
auf HIGH (1) gesetzt wird. Es wird auch eine Meldung "EIN" auf der
Konsole ausgegeben, um den Zustand zu dokumentieren.

Warten für 3 Sekunden:

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)

Hier wird eine kurze Wartezeit von jeweils einer Sekunde eingefügt,
um eine Verzögerung von insgesamt drei Sekunden zu erzeugen. Während
jeder Sekunde wird ein Punkt auf der Konsole ausgegeben, um den
Fortschritt anzuzeigen.

Ausschalten des Relais:

    print('AUS')
    device.off()

    Nach Ablauf der Wartezeit wird das Relais ausgeschaltet, indem der
    GPIO-Pin auf LOW (0) gesetzt wird. Auch hier wird eine entsprechende
    Meldung "AUS" auf der Konsole ausgegeben, um den Zustandswechsel
    zu dokumentieren.

Das Programm dient dazu, die Steuerung eines einfachen Relais über einen
GPIO-Pin auf dem Raspberry Pi Pico zu demonstrieren. Es zeigt, wie man
einen Pin als Ausgang konfiguriert, wie man die Ausgabe ein- und
ausschaltet und wie man Pausen im Programmablauf einfügt.
"""