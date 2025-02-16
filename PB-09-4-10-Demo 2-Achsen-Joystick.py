# Bibliotheken laden
from machine import Pin, ADC
from time import sleep

# Initialisierung: GPIO25 als Ausgang
led_onboard = Pin(25, Pin.OUT, value=0)

# Initialisierung: Button
btn = Pin(22, Pin.IN, Pin.PULL_UP)

# Initialisierung: ADC0 (GPIO26)
adc0 = ADC(0)

# Initialisierung: ADC1 (GPIO27)
adc1 = ADC(1)

# Wiederholung (Endlos-Schleife)
while True:
    # Taster-Zustand
    led_onboard.value(not btn.value())
    # ADC0 als Dezimalzahl lesen (horizontale Achse)
    x = adc0.read_u16()
    # ADC1 als Dezimalzahl lesen (vertikale Achse)
    y = adc1.read_u16()
    # Auswertung der Position/Richtung
    pos_y = 'mitte'
    pos_x = 'mitte'
    if y < 20000: pos_y = 'unten'
    elif y > 40000: pos_y = 'oben'
    if x < 20000: pos_x = 'links'
    elif x > 40000: pos_x = 'rechts'
    # Ausgabe in der Kommandozeile/Shell
    print('ADC0:', x, '/', 'X-Achse:', pos_x)
    print('ADC1:', y, '/', 'Y-Achse:', pos_y)
    print()
    # Warten
    sleep(1)
    
"""
Das vorliegende MicroPython-Programm ist für den Raspberry Pi Pico geschrieben
und zeigt die Verwendung eines Onboard-LEDs, eines Tasters (Button) sowie
zweier analoger Sensoren (ADC0 und ADC1) auf. Das Programm überwacht den Zustand
des Tasters und liest die Werte der beiden analogen Sensoren aus, um deren
Position oder Richtung zu bestimmen. Hier ist eine detaillierte Erläuterung:

    Import von Modulen und Initialisierung:

from machine import Pin, ADC
from time import sleep

    machine: Ein Modul, das Funktionen für Hardwarezugriffe bereitstellt.
    Hier werden die Klassen Pin und ADC verwendet.
    time: Ein Modul zur Zeitmessung. Die Funktion sleep wird verwendet,
    um Pausen im Programmablauf einzufügen.

Initialisierung von Hardwarekomponenten:

led_onboard = Pin(25, Pin.OUT, value=0)
btn = Pin(22, Pin.IN, Pin.PULL_UP)
adc0 = ADC(0)
adc1 = ADC(1)

    led_onboard: Initialisierung der Onboard-LED (GPIO-Pin 25) als Ausgang
    mit einem anfänglichen Wert von 0 (ausgeschaltet).
    btn: Initialisierung des Tasters (GPIO-Pin 22) als Eingang mit
    Pull-Up-Widerstand.
    adc0, adc1: Initialisierung von zwei ADC (Analog-Digital Converter)
    Objekten für die analogen Sensoren an den Pins GPIO26 und GPIO27.

Endlosschleife zur Sensordatenerfassung:

while True:

Die Hauptfunktionalität des Programms findet innerhalb einer Endlosschleife
statt, was bedeutet, dass das Programm kontinuierlich ausgeführt wird.

Taster-Zustandsüberwachung und LED-Steuerung:

led_onboard.value(not btn.value())

Die Onboard-LED wird entsprechend dem Zustand des Tasters (Button) gesteuert.
Wenn der Taster gedrückt wird, wird die LED eingeschaltet und umgekehrt.

Lesen der analogen Sensoren:

x = adc0.read_u16()
y = adc1.read_u16()

Die analogen Sensoren werden ausgelesen. read_u16() gibt den Wert des
ADC als 16-Bit-Ganzzahl zurück.

Auswertung der Sensorwerte:

if y < 29000: pos_y = 'oben'
elif y > 32000: pos_y = 'unten'
if x < 29000: pos_x = 'rechts'
elif x > 32000: pos_x = 'links'

Die Sensorwerte werden ausgewertet, um die Position oder Richtung der Messung zu
bestimmen. Die Schwellenwerte für die Richtung (rechts, links, oben, unten)
sind willkürlich festgelegt und können je nach Anwendung angepasst werden.

Ausgabe der Ergebnisse:

print('ADC0:', x, '/', 'X-Achse:', pos_x)
print('ADC1:', y, '/', 'Y-Achse:', pos_y)
print()

Die erfassten Sensorwerte und deren Positionen werden auf der Konsole ausgegeben.

Warten:

    sleep(1)

    Das Programm wartet eine Sekunde, bevor es den nächsten Schleifendurchlauf beginnt.

Dieses Programm demonstriert die Verwendung von GPIO-Pins, einem Taster und
analogen Sensoren auf dem Raspberry Pi Pico und bietet eine einfache Möglichkeit,
Eingaben von Sensoren zu erfassen und entsprechend zu reagieren.
"""