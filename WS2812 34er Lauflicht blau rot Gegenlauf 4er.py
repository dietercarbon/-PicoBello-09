# Bibliotheken laden
from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms

# GPIO-Pin für WS2812
pin_np = 28

# Anzahl der LEDs
leds = 34

# Helligkeit: 0 bis 255
brightness = 50

# Geschwindigkeit (Millisekunden)
speed = 50

# Initialisierung WS2812/NeoPixel
np = NeoPixel(Pin(pin_np, Pin.OUT), leds)

# Wiederholung (Endlos-Schleife)
while True:
    j=17
    k=17
    for i in range (leds):
        # Nächste LED einschalten
        np[i] = (brightness, brightness, brightness)
        np[leds-i-1] = (brightness, 0, 0)
        
        if i+j >= 34:
            j=-17
        np[i+j] = (brightness, brightness, brightness)
        
        if leds-k-i-1 < 0:
            k=17
        
        np[leds-k-i-1] = (brightness, 0, 0)
        
        np.write()
        sleep_ms(speed)
        # LED zurücksetzen
        np[i] = (0, 0, 0)
        np[leds-i-1] = (0, 0, 0)
        np[i+j] = (0, 0, 0)
        np[leds-k-i-1] = (0, 0, 0)
        
        np.write()
        
        
        