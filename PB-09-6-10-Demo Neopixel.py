# Bibliotheken laden
from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

# GPIO-Pin für WS2812
pin_np = 14

# Anzahl der LEDs
leds = 8

# Helligkeit: 0 bis 255
brightness = 10

# Geschwindigkeit (Millisekunden)
speed = 50

# Initialisierung WS2812/NeoPixel
np = NeoPixel(Pin(pin_np, Pin.OUT), leds)

# Wiederholung (Endlos-Schleife)
while True:
    for i in range (leds):
        # Nächste LED einschalten
        np[i] = (brightness, brightness, brightness)
        np.write()
        sleep_ms(speed)
        # LED zurücksetzen
        np[i] = (0, 0, 0)
        
        """
Das vorliegende MicroPython-Programm ist für den Raspberry Pi Pico
geschrieben und dient dazu, eine Animation auf einem Streifen von
WS2812/NeoPixel-LEDs abzuspielen. Hier ist eine detaillierte Erläuterung:

    Import von Modulen:

    python

from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

    machine: Ein Modul, das Funktionen für Hardwarezugriffe bereitstellt.
    Hier wird die Pin-Klasse verwendet.
    neopixel: Ein Modul zur Steuerung von NeoPixel-LEDs.
    time: Ein Modul zur Zeitmessung. Die Funktion sleep_ms wird verwendet,
    um Pausen in Millisekunden im Programmablauf einzufügen.

Festlegung der Parameter:

python

pin_np = 14
leds = 8
brightness = 10
speed = 50

    pin_np: GPIO-Pin, der mit dem Datenpin des WS2812/NeoPixel-Streifens
    verbunden ist (hier GPIO-Pin 14).
    leds: Anzahl der LEDs im Streifen (hier 8).
    brightness: Helligkeit der LEDs, ein Wert zwischen 0 und 255 (hier 10).
    speed: Geschwindigkeit der Animation in Millisekunden (hier 50).

Initialisierung des NeoPixel-Streifens:

np = NeoPixel(Pin(pin_np, Pin.OUT), leds)

Hier wird der NeoPixel-Objekt erstellt und mit dem angegebenen Pin und
der Anzahl der LEDs initialisiert.

Endlosschleife für die Animation:

while True:

Die Animation wird in einer Endlosschleife abgespielt, was bedeutet,
dass sie kontinuierlich wiederholt wird.

Animation der LEDs:

    for i in range(leds):
        np[i] = (brightness, brightness, brightness)
        np.write()
        sleep_ms(speed)
        np[i] = (0, 0, 0)

    Diese Schleife durchläuft jede LED im Streifen. Für jede LED wird
    die Helligkeit auf den angegebenen Wert gesetzt, die Farbe ist hier
    weiß. Dann wird np.write() aufgerufen, um die Änderungen auf die LEDs
    anzuwenden. Danach wird eine kurze Pause von speed Millisekunden
    eingefügt, um die Animation sichtbar zu machen. Anschließend wird die
    LED zurückgesetzt, indem die Farbe auf Schwarz gesetzt wird.

Dieses Programm dient dazu, eine einfache Animation auf einem Streifen von
NeoPixel-LEDs zu erzeugen. Es kann leicht angepasst werden, um unterschiedliche
Animationen oder Effekte zu erzeugen, indem die Parameter wie Anzahl der LEDs,
Helligkeit und Geschwindigkeit geändert werden.
"""