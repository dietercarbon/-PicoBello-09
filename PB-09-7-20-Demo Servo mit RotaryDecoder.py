# Bibliotheken laden
from machine import Pin, PWM
from rotary import Rotary
import time

# GPIO für Steuersignal
servo_pin = 6

# GPIOs zum Rotary Encoder
pin_dt = 2
pin_clk = 3
pin_sw = 4

# Wert für 0 Grad
valueMin = 0

# Wert für 180 Grad
valueMax = 180

# Position in Grad
value = 90

# Positionsänderung in Grad
step = 10

# Initialiserung Rotary Encoder
rotary = Rotary(pin_dt, pin_clk, pin_sw)

# Initialisierung PWM-Signal
servo = PWM(Pin(servo_pin))
servo.freq(50)

# Funktion
def rotary_changed(change):
    global value, valueMin, valueMax, step
    if change == Rotary.ROT_CW:
        value = value + step
        print('Rechts')
    elif change == Rotary.ROT_CCW:
        value = value - step
        print('Links')
    # Begrenzung des Wertebereichs
    if value < valueMin: value = valueMin
    if value > valueMax: value = valueMax
    servo_control(value)

# Funktion: Servo steuern
def servo_control(value, minDuty=1638, maxDuty=8192):
    # Tastverhältnis berechnen
    newDuty = int(maxDuty - (value - valueMin) * (maxDuty - minDuty) / (valueMax - valueMin) )
    # Datenausgabe
    print('Grad:', value)
    print('Duty:', newDuty)
    print()
    # PWM-Signal ändern
    servo.duty_u16(newDuty)

# Hauptprogramm
print('STRG + C zum Benden')
print()

try:
    # Grundposition
    servo_control(value)
    # Wenn der Encoder bedient wird
    rotary.add_handler(rotary_changed)
    # Wiederholung (damit das Programm weiterläuft)
    while True:
        time.sleep(1)
except (KeyboardInterrupt):
    pass
finally:
    servo.deinit()
    print('Beendet')
    
"""
Das vorliegende MicroPython-Programm steuert ebenfalls einen Servo-Motor
mit einem Rotary Encoder, aber es verwendet eine andere Methode zur Berechnung
und Anpassung der Servo-Positionen über das PWM-Signal. Hier sind die
Hauptunterschiede im Vergleich zum vorherigen Programm:

    Servo-Steuerungsmethode:
        Im vorherigen Programm werden feste PWM-Werte für verschiedene
        Positionen des Servo-Motors definiert und direkt in den Code eingefügt.
        Im aktuellen Programm wird eine Funktion servo_control definiert, um
        das PWM-Signal basierend auf dem aktuellen Wert (Grad) zu berechnen
        und anzupassen. Diese Funktion verwendet eine lineare Interpolation
        zwischen einem minimalen und einem maximalen PWM-Wert, um den
        Duty Cycle des PWM-Signals zu berechnen, der die aktuelle Position
        des Servo-Motors repräsentiert.

    Rotary Encoder Handling:
        Im vorherigen Programm wird der Rotary Encoder verwendet, um die
        PWM-Geschwindigkeit anzupassen, während die Position des Servo-Motors
        direkt im Code festgelegt ist.
        Im aktuellen Programm wird der Rotary Encoder verwendet, um die Position
        des Servo-Motors direkt zu steuern. Jede Drehung des Encoders ändert
        den Gradwert, der dann zur Berechnung des entsprechenden PWM-Duty-Cycles
        verwendet wird.

    Anpassung der Servo-Position:
        Im vorherigen Programm werden die Positionen des Servo-Motors direkt
        durch feste PWM-Werte für verschiedene Winkel definiert.
        Im aktuellen Programm können die Servo-Positionen durch die Benutzung
        des Rotary Encoders kontinuierlich und in kleinen Schritten (10 Grad)
        angepasst werden. Dies ermöglicht eine feinere Steuerung und Einstellung
        der Servo-Position.

    Programmausführung:
        Beide Programme enthalten eine Endlosschleife, die durch eine
        Tastaturunterbrechung (Strg + C) beendet werden kann.
        Im aktuellen Programm wird die Position des Servo-Motors kontinuierlich
        überwacht und angepasst, solange das Programm läuft, während im vorherigen
        Programm der Servo-Motor in vordefinierten Positionen bewegt wird und das
        Programm dann endet.

Insgesamt ermöglicht das aktuelle Programm eine dynamische und präzise Steuerung
der Servo-Positionen über den Rotary Encoder, während das vorherige Programm eine
einfache Sequenz von vordefinierten Positionen abarbeitet. Die Wahl zwischen den
beiden hängt von den Anforderungen des Projekts und der gewünschten
Steuerungspräzision ab.

"""