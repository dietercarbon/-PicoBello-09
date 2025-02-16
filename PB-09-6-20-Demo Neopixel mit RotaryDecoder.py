# Bibliotheken laden
from machine import Pin
from neopixel import NeoPixel
from rotary import Rotary
from utime import sleep_ms

# GPIO-Pin für WS2812
pin_np = 14

# Anzahl der LEDs
leds = 8

# Helligkeit: 0 bis 255
brightness = 5

# Geschwindigkeit (Millisekunden)
speed = 100

# Initialisierung WS2812/NeoPixel
np = NeoPixel(Pin(pin_np, Pin.OUT), leds)

# GPIO-Pins für Encoder
pin_dt = 2
pin_clk = 3
pin_sw = 4

# Initialiserung Rotary Encoder
rotary = Rotary(pin_dt, pin_clk, pin_sw)
for i in range (leds): np[i] = (0, 0, 0)

# Funktion
def rotary_changed(change):
    global speed
    if change == Rotary.ROT_CW:
        speed = speed - 5
    elif change == Rotary.ROT_CCW:
        speed = speed + 5
    # Korrektur, wenn Ende erreicht
    if speed < 5: speed = 5
    # Korrektur, wenn Anfang erreicht
    if speed > 500: speed = 500
    print(speed)

# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)

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
Dieses MicroPython-Programm ist für den Raspberry Pi Pico geschrieben und
steuert einen WS2812/NeoPixel-LED-Streifen basierend auf den Eingaben
eines Rotary Encoders. Hier ist eine detaillierte Erläuterung:

    Import von Modulen:

    python

from machine import Pin
from neopixel import NeoPixel
from rotary import Rotary
from utime import sleep_ms

    machine: Ein Modul, das Funktionen für Hardwarezugriffe bereitstellt.
    Hier wird die Pin-Klasse verwendet.
    neopixel: Ein Modul zur Steuerung von NeoPixel-LEDs.
    rotary: Ein Modul zur Steuerung des Rotary Encoders.
    utime: Ein Modul zur Zeitmessung. Die Funktion sleep_ms wird verwendet,
    um Pausen in Millisekunden im Programmablauf einzufügen.

Festlegung der Parameter:

python

pin_np = 14
leds = 8
brightness = 5
speed = 100

    pin_np: GPIO-Pin, der mit dem Datenpin des WS2812/NeoPixel-Streifens
    verbunden ist (hier GPIO-Pin 14).
    leds: Anzahl der LEDs im Streifen (hier 8).
    brightness: Helligkeit der LEDs, ein Wert zwischen 0 und 255 (hier 5).
    speed: Geschwindigkeit der Animation in Millisekunden (hier 100).

Initialisierung des WS2812/NeoPixel-Streifens:

python

np = NeoPixel(Pin(pin_np, Pin.OUT), leds)

Hier wird der NeoPixel-Objekt erstellt und mit dem angegebenen Pin und der
Anzahl der LEDs initialisiert. Alle LEDs werden zunächst ausgeschaltet,
indem ihre Farben auf Schwarz gesetzt werden.

Initialisierung des Rotary Encoders:

python

rotary = Rotary(pin_dt, pin_clk, pin_sw)

Hier wird eine Instanz des Rotary Encoders erstellt und mit den angegebenen
Pins initialisiert.

Funktionsdefinition für die Verarbeitung der Encoder-Ereignisse:

python

def rotary_changed(change):
    global speed
    # Verarbeitung der Encoder-Ereignisse
rotary.add_handler(rotary_changed)

Die Funktion rotary_changed wird definiert, um die Ereignisse des Rotary
Encoders zu verarbeiten. Sie aktualisiert die Geschwindigkeit der Animation
basierend auf der Drehrichtung des Encoders. Die Geschwindigkeit wird
um +/-5 Millisekunden geändert, wenn der Encoder im Uhrzeigersinn bzw.
gegen den Uhrzeigersinn gedreht wird. Die Geschwindigkeit wird auf einen
Mindestwert von 5 Millisekunden begrenzt und auf einen Höchstwert
von 500 Millisekunden begrenzt.

Hauptschleife zur Animation der LEDs:

python

    while True:
        for i in range (leds):
            # Nächste LED einschalten
            np[i] = (brightness, brightness, brightness)
            np.write()
            sleep_ms(speed)
            # LED zurücksetzen
            np[i] = (0, 0, 0)

    Diese Schleife wird kontinuierlich ausgeführt. Für jede LED im Streifen
    wird die Helligkeit auf den angegebenen Wert gesetzt und dann für
    die Dauer der angegebenen Geschwindigkeit eingeschaltet.
    Anschließend wird die LED wieder ausgeschaltet.

Das Programm ermöglicht es dem Benutzer, die Geschwindigkeit der LED-Animation
durch Drehen des Rotary Encoders anzupassen, wodurch eine interaktive Steuerung
der Animation ermöglicht wird.
"""