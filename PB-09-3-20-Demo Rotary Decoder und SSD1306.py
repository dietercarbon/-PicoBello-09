# Bibliotheken laden
from rotary import Rotary
from utime import sleep
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C


# Initialisiere I2C
i2c_dev = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Initialisiere SSD1306 Display
oled = SSD1306_I2C(128,64, i2c_dev) # oled controller

# GPIOs zum Rotary Encoder
pin_dt = 18
pin_clk = 19
pin_sw = 17

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

print("44")

oled.fill(0)
oled.text("Moin, mein Test:", 0, 0)
oled.text("*** SetUp ***", 0, 10)
oled.show()

#oled.fill_rect(0, 40, 128, 10, 0)  # (x, y, width, height, color)
#oled.text("Eingabe: {:>6.0f}".format(value), 0, 40)
#oled.show()

#Jahr eingeben
value=2020
while weiter == False:
    print(value)
    strValue = str(value)
    oled.fill_rect(0, 20, 128, 10, 0)  # (x, y, width, height, color)
    oled.text("Jahr: "+strValue, 0, 20)
    oled.show()
    sleep(.1)
Jahr=value
print("Jahr: ", Jahr)
weiter = False

    
#Monat eingeben
value=1
while weiter == False:
    print(value)
    strValue = str(value)
    oled.fill_rect(0, 30, 128, 10, 0)  # (x, y, width, height, color)
    if len(strValue)==1:
        oled.text("Monat:   "+strValue, 0, 30)
    elif len(strValue)==2:
        oled.text("Monat:  "+strValue, 0, 30)
    oled.show()
    sleep(.1)
Monat=value
print("Monat: ", Monat)
weiter = False
    
#Tag eingeben
value=15
while weiter == False:
    print(value)
    strValue = str(value)
    oled.fill_rect(0, 40, 128, 10, 0)  # (x, y, width, height, color)
    if len(strValue)==1:
        oled.text("Tag:     "+strValue, 0, 40)
    elif len(strValue)==2:
        oled.text("Tag:    "+strValue, 0, 40)
    oled.show()
    sleep(.1)
Tag=value
print("Tag: ", Tag)
weiter = False

oled.fill_rect(0, 56, 128, 10, 0)  # (x, y, width, height, color)
Datum = "Date: "+str(Tag)+"."+str(Monat)+"."+str(Jahr)
oled.text(Datum, 0, 56)
oled.show()


    
'''
#Stunde eingeben
value=1
while weiter == False:
    print(value)
    sleep(.1)
Stunde=value
print("Stunde: ", Stunde)
weiter = False
    
#Minute eingeben
value=1
while weiter == False:
    print(value)
    sleep(.1)
Minute=value
print("Minute: ", Minute)
'''

# Statt den Handler zu entfernen, eine leere Funktion setzen
def ignore_rotary(change):
    pass

rotary.add_handler(ignore_rotary)  # Ersetzt den alten Handler
print("Rotary deaktiviert.")


"""
### Beschreibung des Programms ###

Dieses Programm läuft auf einem Raspberry Pi Pico und ermöglicht die Eingabe eines Datums
(Jahr, Monat, Tag) mithilfe eines Drehencoders (Rotary Encoder). Das eingegebene Datum
wird auf einem SSD1306 OLED-Display angezeigt.

### Hardware:
- **Raspberry Pi Pico**
- **Rotary Encoder** mit drei GPIO-Verbindungen:
  - `pin_dt = 18` (Datenleitung)
  - `pin_clk = 19` (Taktleitung)
  - `pin_sw = 17` (Taster)
- **SSD1306 OLED-Display**, angeschlossen über I2C:
  - `SCL = Pin 5`
  - `SDA = Pin 4`

### Funktionsweise:
1. **Initialisierung:** 
   - Der I2C-Bus wird konfiguriert
   - Das OLED-Display wird initialisiert
   - Der Rotary Encoder wird eingerichtet

2. **Eingabeprozess:**
   - Der Rotary Encoder kann gedreht werden, um Werte zu erhöhen oder zu verringern
   - Beim Drücken des Encoders wird die Eingabe bestätigt
   - Der Benutzer gibt **nacheinander das Jahr, den Monat und den Tag** ein

3. **Anzeige des Datums:**
   - Das eingegebene Datum wird auf dem OLED-Display angezeigt
   - Nach der letzten Eingabe werden weitere Eingaben vom Rotary Encoder ignoriert

### Steuerung:
- **Drehen nach rechts:** Wert erhöhen
- **Drehen nach links:** Wert verringern
- **Drücken des Encoders:** Eingabe bestätigen

### Deaktivierung des Encoders:
Nach Abschluss der Eingabe wird der Rotary Encoder deaktiviert, sodass keine weiteren
Änderungen mehr möglich sind.

"""


