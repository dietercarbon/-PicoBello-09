# Bibliotheken laden
from rotary import Rotary
from utime import sleep
import tm1637
from time import sleep_ms
from machine import I2C, Pin

display = tm1637.TM1637(clk=Pin(0), dio=Pin(1))

# GPIOs zum Rotary Encoder
pin_dt = 2
pin_clk = 3
pin_sw = 4

# Initialiserung Rotary Encoder
rotary = Rotary(pin_dt, pin_clk, pin_sw)
value = 0
weiter = False

# Funktion
def rotary_changed(change):
    global value
    global weiter
    if change == Rotary.ROT_CW:
        value = value + 1
        print('Rechts (', value, ')')
    elif change == Rotary.ROT_CCW:
        value = value - 1
        print('Links (', value, ')')
    elif change == Rotary.SW_PRESS:
        print('Gedrückt')
        weiter = True
        #value = 0
    elif change == Rotary.SW_RELEASE:
        print('Losgelassen')

# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)

# ====================================================
#Datum und Uhrzeit eingeben
# ====================================================

#Jahr eingeben
value=2020
while weiter == False:
    print(value," (Jahr bis 2050)")
    display.number(value)
    sleep(.1)
Jahr=value
print("Jahr: ", Jahr)
weiter = False
# ====================================================
    
#Monat eingeben
value=6
display.show("    ")
while weiter == False:
    print(value," (Monat bis 12)")
    display.number(value)
    sleep(.1)
Monat=value
print("Monat: ", Monat)
weiter = False
# ====================================================
    
#Tag eingeben
value=15
display.show("    ")
while weiter == False:
    print(value," (Tag bis 31)")
    display.number(value)
    sleep(.1)
Tag=value
print("Tag: ", Tag)
weiter = False
# ====================================================
    
#Stunde eingeben
value=12
display.show("    ")
while weiter == False:
    print(value," (Stunde bis 23)")
    display.number(value)
    sleep(.1)
Stunde=value
print("Stunde: ", Stunde)
weiter = False
# ====================================================
    
#Minute eingeben
value=30
display.show("    ")
while weiter == False:
    print(value," (Minute bis 59)")
    display.number(value)
    sleep(.1)
Minute=value
print("Minute: ", Minute)
print()
print()
# ====================================================

print("Eingaben:")
print("Jahr: ", Jahr)
print("Monat: ", Monat)
print("Tag: ", Tag)
print("Stunde: ", Stunde)
print("Minute: ", Minute)

"""
Das vorliegende Python-Programm ist für den Raspberry Pi Pico geschrieben und verwendet
die MicroPython-Plattform. Es interagiert mit einem Rotary-Encoder und einem TM1637-Display,
um Benutzereingaben für das Datum und die Uhrzeit zu erfassen.

Hier ist eine detaillierte Erläuterung des Programms:

    Import von Modulen:

from rotary import Rotary
from utime import sleep
import tm1637
from time import sleep_ms
from machine import I2C, Pin

    Rotary: Ein Modul zur Steuerung des Rotary-Encoders.
    utime: Modul zur Zeitmessung, wird verwendet, um Pausen im Programmablauf einzufügen.
    tm1637: Modul zur Steuerung des TM1637-Displays.
    machine: Ein Modul, das Funktionen für Hardwarezugriffe bereitstellt. Hier wird
    die Pin-Klasse verwendet, um die Pins des Raspberry Pi Pico zu steuern, und I2C, um
    die I2C-Kommunikation zu ermöglichen.

Initialisierung des Displays:

display = tm1637.TM1637(clk=Pin(0), dio=Pin(1))

Eine Instanz der TM1637-Klasse wird erstellt und mit den Pins 0 (clk) und 1 (dio) verbunden,
um die Kommunikation mit dem Display zu ermöglichen.

Konfiguration des Rotary Encoders:

pin_dt = 2
pin_clk = 3
pin_sw = 4
rotary = Rotary(pin_dt, pin_clk, pin_sw)

Hier werden die Pins für den Rotary Encoder festgelegt und eine Instanz der Rotary-Klasse
erstellt, um die Eingaben des Encoders zu verarbeiten.

Funktionsdefinition für die Verarbeitung der Encoder-Ereignisse:

    def rotary_changed(change):
        global value
        global weiter
        # Verarbeitung der Encoder-Ereignisse
    rotary.add_handler(rotary_changed)

    Die Funktion rotary_changed wird definiert, um die Ereignisse des Rotary Encoders
    zu verarbeiten. Sie aktualisiert den globalen Wert value je nach Drehrichtung und
    reagiert auf Druck- und Loslass-Ereignisse des Encoder-Tasters.

    Erfassung von Datum und Uhrzeit:
    Die Benutzereingaben für Jahr, Monat, Tag, Stunde und Minute werden nacheinander erfasst.
    Der Rotary Encoder wird verwendet, um die Werte auszuwählen, und das TM1637-Display zeigt
    den ausgewählten Wert an. Die Eingaben werden durch Drücken des Rotary-Tasters bestätigt.

    Anzeigen der Eingaben:
    Nachdem alle Eingaben erfasst wurden, werden sie auf der Konsole ausgegeben, um dem
    Benutzer eine Bestätigung zu geben.

Das Programm ermöglicht es dem Benutzer, das Datum und die Uhrzeit über den Rotary-Encoder
einzugeben und die Eingaben auf dem TM1637-Display anzuzeigen.


"""



