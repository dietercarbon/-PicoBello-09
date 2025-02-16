# Bibliotheken laden
from time import sleep
from picodfplayer import DFPlayer

# Initialisierung DFPlayer (UART, TX-Pin, RX-Pin, Busy-Pin)
player = DFPlayer(0, 16, 17, 18)
sleep(1)
player.setVolume(30) # Lautstärke einstellen: 0 bis 30

# Titel-Zähler
count = 1

print('Abspielen:', count)
# Verzeichnis: 01 / Datei: 001 (/01/001)
player.playTrack(1,1)

# Wiederholung: Endlos-Schleife
while True:
    sleep(5)
    player.nextTrack()
        
"""
Dieses MicroPython-Programm ist für den Raspberry Pi Pico geschrieben und
dient dazu, MP3-Dateien mit dem DFPlayer Mini MP3-Modul abzuspielen.
Hier ist eine detaillierte Erläuterung:

    Import von Modulen:

from time import sleep
from picodfplayer import DFPlayer

    time: Ein Modul zur Zeitmessung. Die Funktion sleep wird verwendet,
    um Pausen im Programmablauf einzufügen.
    picodfplayer: Ein benutzerdefiniertes Modul zur Steuerung des
    DFPlayer Mini MP3-Moduls über UART.

Initialisierung des DFPlayer Mini:

player = DFPlayer(0, 16, 17, 18)

Hier wird eine Instanz des DFPlayer Mini-Objekts erstellt und mit den
entsprechenden Pins für UART, TX, RX und Busy initialisiert. Der Busy-Pin
wird verwendet, um den Status des DFPlayer Mini (z. B. Wiedergabe beendet)
abzufragen.

Einstellen der Lautstärke:

player.setVolume(15)

Die Lautstärke wird auf einen festen Wert von 15 (auf einer Skala von 0 bis 30)
eingestellt.

Abspielen des ersten Titels:

player.playTrack(1,1)

Hier wird der erste Titel von der MP3-Datei im Verzeichnis 01 und mit der
Dateinummer 001 abgespielt.

Abspielen von weiteren Titeln in Endlosschleife:

while True:
    sleep(5)
    if player.queryBusy() == False:
        count += 1
        player.nextTrack()

In dieser Endlosschleife wird in einem Intervall von 5 Sekunden überprüft,
ob der aktuelle Titel beendet ist. Wenn der DFPlayer Mini nicht mehr "beschäftigt"
ist (d. h. der aktuelle Titel ist beendet), wird der nächste Titel abgespielt.
Der Titelzähler wird inkrementiert, um den aktuellen Titel zu verfolgen.

Titelzähler und Ausgabe:

    count = 1
    print('Abspielen:', count)

    Hier wird der Titelzähler initialisiert und der erste abzuspielende
    Titel angekündigt. Während des Abspielens wird der Titelzähler bei
    jedem Titelwechsel aktualisiert und auf der Konsole ausgegeben.

Zusammenfassend spielt dieses Programm MP3-Dateien in Endlosschleife mit
dem DFPlayer Mini MP3-Modul ab, wobei es einen einfachen Mechanismus zur
Überwachung und Steuerung der Wiedergabe bietet.
"""