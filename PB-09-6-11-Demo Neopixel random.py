# Bibliotheken laden
from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms
import random
# GPIO-Pin für WS2812
pin_np = 14

# Anzahl der LEDs
leds = 8

# Helligkeit: 0 bis 255
brightness = 20

# Geschwindigkeit (Millisekunden)
speed = 50

# Initialisierung WS2812/NeoPixel
np = NeoPixel(Pin(pin_np, Pin.OUT), leds)

# Wiederholung (Endlos-Schleife)
while True:
    for i in range (leds):
        # Nächste LED einschalten
        #np[i] = (brightness, brightness, brightness)
        np[i] = (int(random.random()*brightness), int(random.random()*brightness), int(random.random()*brightness))
        np.write()
        sleep_ms(speed)
        # LED zurücksetzen
        np[i] = (0, 0, 0)
        
"""
Die beiden Programme verwenden das NeoPixel-Modul, um Animationen auf einem
Streifen von WS2812/NeoPixel-LEDs auf dem Raspberry Pi Pico abzuspielen.
Der Hauptunterschied zwischen den beiden Programmen liegt jedoch in der
Art und Weise, wie die Farben für die LEDs generiert werden.

Im ersten Programm werden alle LEDs nacheinander auf eine feste Farbe
gesetzt (hier weiß mit einer bestimmten Helligkeit), bevor sie wieder
ausgeschaltet werden. Dies erzeugt eine Animation, bei der jede LED
kurzzeitig aufleuchtet und dann wieder erlischt. Die Helligkeit und
Geschwindigkeit der Animation können durch die entsprechenden Parameter
festgelegt werden.

Im zweiten Programm hingegen werden die Farben der LEDs zufällig generiert.
Anstelle einer festen Farbe werden für jede LED zufällige RGB-Werte (Rot, Grün, Blau)
zwischen 0 und der angegebenen Helligkeit generiert. Dies führt zu einer dynamischen
Animation, bei der die LEDs in zufälligen Farben aufleuchten und wieder erlöschen.
Durch die Verwendung von Zufallsfarben entsteht eine abwechslungsreiche und
interessante visuelle Wirkung.

Zusammenfassend lässt sich sagen, dass das erste Programm eine statische
Animation mit festen Farben erzeugt, während das zweite Programm eine dynamische
Animation mit zufällig generierten Farben erzeugt. Die Wahl zwischen den beiden
hängt von den gewünschten visuellen Effekten und dem gewünschten Verhalten
der LED-Animation ab.
"""