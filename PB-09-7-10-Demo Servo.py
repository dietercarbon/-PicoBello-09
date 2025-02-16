# Bibliotheken laden
from machine import Pin, PWM
from time import sleep

# GPIO für Steuersignal
servo_pin = 6

# 0 Grad
grad000 = 500000
# 45 Grad
grad045 = 1000000
# 90 Grad
grad090 = 1500000
# 135 Grad
grad135 = 2000000
# 180 Grad
grad180 = 2500000

pwm = PWM(Pin(servo_pin))
pwm.freq(50)

print('Position: Mitte (90 Grad)')
pwm.duty_ns(grad090)
sleep(2)

print('Position: Ganz Links (0 Grad)')
pwm.duty_ns(grad000)
sleep(2)

print('Position: Mitte (90 Grad)')
pwm.duty_ns(grad090)
sleep(2)

print('Position: Ganz Rechts (180 Grad)')
pwm.duty_ns(grad180)
sleep(2)

print('Position: Mitte (90 Grad)')
pwm.duty_ns(grad090)
sleep(2)

pwm.deinit()
print('Ende')


"""
Das vorliegende MicroPython-Programm ist für den Raspberry Pi Pico geschrieben
und steuert ein Servo-Motor durch die Veränderung des Pulsweitenmodulation (PWM)
Signals. Hier ist eine detaillierte Erläuterung:

    Import von Modulen:

from machine import Pin, PWM
from time import sleep

    machine: Ein Modul, das Funktionen für Hardwarezugriffe bereitstellt.
    Hier werden die Klassen Pin und PWM verwendet.
    time: Ein Modul zur Zeitmessung. Die Funktion sleep wird verwendet, um
    Pausen im Programmablauf einzufügen.

Festlegung des GPIO-Pins für das Servo-Signal:

servo_pin = 6

Hier wird der GPIO-Pin festgelegt, der für das Servo-Signal verwendet
wird (hier GPIO-Pin 6).

Definition der PWM-Werte für verschiedene Positionen des Servo-Motors:

grad000 = 500000   # 0 Grad
grad045 = 1000000  # 45 Grad
grad090 = 1500000  # 90 Grad
grad135 = 2000000  # 135 Grad
grad180 = 2500000  # 180 Grad

Diese Werte repräsentieren die Pulsweiten in Nanosekunden, die den verschiedenen
Winkelpositionen des Servo-Motors entsprechen. Sie sind typischerweise
herstellerspezifisch und können je nach Servo variieren.

Initialisierung des PWM-Signals:

pwm = PWM(Pin(servo_pin))
pwm.freq(50)

Hier wird ein PWM-Objekt erstellt und mit dem angegebenen GPIO-Pin initialisiert.
Die Frequenz des PWM-Signals wird auf 50 Hz festgelegt, was dem Standardwert
für Servo-Motoren entspricht.

Ansteuerung des Servo-Motors:

print('Position: Mitte (90 Grad)')
pwm.duty_ns(grad090)
sleep(2)

print('Position: Ganz Links (0 Grad)')
pwm.duty_ns(grad000)
sleep(2)

print('Position: Mitte (90 Grad)')
pwm.duty_ns(grad090)
sleep(2)

print('Position: Ganz Rechts (180 Grad)')
pwm.duty_ns(grad180)
sleep(2)

print('Position: Mitte (90 Grad)')
pwm.duty_ns(grad090)
sleep(2)

Der Servo-Motor wird nacheinander in verschiedenen Positionen bewegt.
Zuerst wird er in die Mitte (90 Grad) bewegt, dann ganz nach links (0 Grad),
wieder zurück in die Mitte, dann ganz nach rechts (180 Grad) und schließlich
erneut zurück in die Mitte. Zwischen den Bewegungen gibt es jeweils
eine Pause von 2 Sekunden.

Deinitialisierung des PWM-Signals:

    pwm.deinit()
    print('Ende')

    Nachdem alle Positionen durchlaufen sind, wird das PWM-Objekt
    deinitialisiert, um die GPIO-Ressourcen freizugeben.
    Eine Abschlussmeldung wird auf der Konsole ausgegeben.

Dieses Programm dient dazu, die Steuerung eines Servo-Motors über PWM-Signale
zu demonstrieren und zeigt, wie man den Servo-Motor auf verschiedene
Positionen bewegt. Die genauen PWM-Werte müssen möglicherweise an die
Spezifikationen des verwendeten Servo-Motors angepasst werden.



Die verschiedenen PWM-Werte, die im Programm für die verschiedenen Positionen
des Servo-Motors verwendet werden, basieren auf der Funktionsweise von
Servo-Motoren und dem PWM-Signal, das sie steuert. Hier ist eine detaillierte
Erklärung, wie die PWM-Werte die Positionen des Servo-Motors beeinflussen:

    Servo-Motoren und PWM-Signale:
    Servo-Motoren werden typischerweise mit PWM (Pulsweitenmodulation) gesteuert.
    Ein Servo-Motor kann in einen bestimmten Winkelposition bewegt werden, je
    nachdem, wie lange das PWM-Signal anliegt und wie lange es ausgeschaltet
    ist. Das PWM-Signal besteht aus einer Folge von Impulsen, deren
    Länge (Pulsweite) variiert, um den Motor in eine bestimmte Position zu bringen.

    Pulsweitenmodulation (PWM):
    PWM ist eine Methode zur Erzeugung eines analogen Signals mit Hilfe
    eines digitalen Signals. Das Signal besteht aus einer Reihe von Impulsen,
    wobei die Länge des Impulses (Pulsweite) variiert, während die Frequenz
    konstant bleibt. Die Pulsweite steuert den Durchschnittswert des Signals
    und damit die Ausgangsleistung des Motors.

    Pulsweiten für verschiedene Positionen:
    Die Servo-Motorposition wird durch die Pulsweite des PWM-Signals gesteuert.
    Die genaue Zuordnung zwischen Pulsweite und Position kann je nach Servo-Modell
    variieren, aber im Allgemeinen gelten folgende Konventionen:
        Ein PWM-Signal mit einer Pulsweite von 1,5 ms (Millisekunden) bewegt
        den Servo-Motor in die Mitte, was typischerweise 90 Grad entspricht.
        Eine Pulsweite von weniger als 1,5 ms bewegt den Servo-Motor in
        Richtung seiner minimalen Position (z. B. 0 Grad).
        Eine Pulsweite von mehr als 1,5 ms bewegt den Servo-Motor in Richtung
        seiner maximalen Position (z. B. 180 Grad).

    Die genauen Pulsweiten für bestimmte Winkel hängen von der Spezifikation des
    Servo-Motors ab und können durch Experimentieren oder durch Bezugnahme auf
    das Datenblatt des Servos ermittelt werden.

    PWM-Werte im Programm:
    Die im Programm verwendeten PWM-Werte grad000, grad045, grad090, grad135
    und grad180 sind die Pulsweiten in Nanosekunden, die den verschiedenen
    Positionen des Servo-Motors entsprechen. Diese Werte sind so festgelegt,
    dass sie die gewünschten Winkelpositionen repräsentieren, wie im Datenblatt
    des Servo-Motors angegeben oder durch Experimentieren ermittelt.

Insgesamt werden die verschiedenen Positionen des Servo-Motors im Programm
durch die Verwendung von PWM-Signalen mit unterschiedlichen Pulsweiten gesteuert,
wobei jede Pulsweite einer bestimmten Winkelposition entspricht.
"""