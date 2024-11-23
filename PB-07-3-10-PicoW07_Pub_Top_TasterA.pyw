#==========================================================================
#
# PB-07-3-10-PicoW07_Pub_Top_TasterA.pyw
#
#  1 Taster (TasterA)
#
#  onboard LED:
#  Z47  *  =  WLAN Verbindung erfolgreich hergestellt
#  Z53  **  =  MQTT-Client erfolgreich erstellt
#  Z61  ***  =  "on" ge-publisht
#
#  Z28  MQTT_TOPIC = "TasterA"
#  Z50  client = MQTTClient("PicoW11", MQTT_BROKER)
#
#==========================================================================
#
# Bibliotheken laden
import machine
import network
from time import sleep
from simple import MQTTClient
from Zugang_DC import wlanSSID, wlanPW, IP_MQTT_broker

# WLAN-Zugangsdaten und MQTT-Broker-Details
WIFI_SSID = wlanSSID()
WIFI_PASSWORD = wlanPW()
MQTT_BROKER = IP_MQTT_broker()
MQTT_TOPIC = "TasterA"

# Initialisieren des Taster-Pins und LED-Anzeige
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
LED = machine.Pin("LED", machine.Pin.OUT)

def LED_blinkt(Zahl):
    for Nummer in range(Zahl):
        LED.value(1);sleep(0.3);LED.value(0);sleep(0.2)
    return 

# Verbindung zum WLAN herstellen
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)
while not wifi.isconnected():
    sleep(0.1)

Blinki = 1 ;LED_blinkt(Blinki); print("LED_blinkt ", Blinki);sleep(1)
#  *  =  WLAN Verbindung erfolgreich hergestellt

# MQTT-Client erstellen
client = MQTTClient("PicoW11", MQTT_BROKER)

Blinki = 2 ;LED_blinkt(Blinki); print("LED_blinkt ", Blinki);sleep(1)
#  **  =  MQTT-Client erfolgreich erstellt

# Hauptprogramm
while True:
    if button.value() == 0:
        client.connect()
        client.publish(MQTT_TOPIC, "Taster A on")
        Blinki = 3 ;LED_blinkt(Blinki); print("LED_blinkt ", Blinki);sleep(1)
        #  ***  =  "on" ge-publisht
        client.disconnect()
        sleep(0.5)
    else:
        sleep(0.1)
        
        
"""
Dieses Programm ist in der Programmiersprache MicroPython geschrieben und soll
den Status eines Tasters überwachen und diesen Status über das MQTT-Protokoll an
einen MQTT-Broker senden. Hier ist eine detaillierte Erläuterung des Programms:

    Das Programm beginnt mit Kommentaren, die Informationen über den Namen
    des Programms, den verwendeten Taster und die Bedeutung der onboard LED enthalten.

    Es werden die benötigten Bibliotheken importiert:
        machine: Eine Bibliothek, die Funktionen zur Steuerung von Hardwarekomponenten
        bereitstellt.
        network: Eine Bibliothek zur Verbindung mit WLAN-Netzwerken.
        time.sleep: Eine Funktion zum Einbauen von Verzögerungen im Programmablauf.
        simple.MQTTClient: Eine vereinfachte MQTT-Client-Bibliothek.
        Zugang_DC: Eine benutzerdefinierte Bibliothek, die Zugangsdaten für WLAN und
        den MQTT-Broker enthält.

    Es werden Variablen definiert, die die WLAN-Zugangsdaten und die MQTT-Broker-Details
    enthalten.

    Der Taster-Pin und die LED werden initialisiert. Der Taster wird als Eingangspin
    mit Pull-up-Widerstand konfiguriert, um den Zustand des Tasters zu überwachen.
    Die LED wird verwendet, um den Status der Verbindung und das Publizieren
    von MQTT-Meldungen anzuzeigen.

    Es wird eine Funktion LED_blinkt(Zahl) definiert, die die LED eine bestimmte Anzahl
    von Malen blinken lässt. Dies dient dazu, den aktuellen Status des Programms anzuzeigen.

    Eine Verbindung zum WLAN wird hergestellt. Die WLAN-Zugangsdaten werden verwendet,
    um sich mit dem WLAN-Netzwerk zu verbinden. Das Programm wartet in einer Schleife,
    bis die Verbindung hergestellt ist.

    Die LED blinkt einmal auf, um anzuzeigen, dass die WLAN-Verbindung erfolgreich
    hergestellt wurde.

    Ein MQTT-Client wird erstellt. Der Client wird mit dem Namen "PicoW11" und
    den MQTT-Broker-Details initialisiert.

    Die LED blinkt zweimal auf, um anzuzeigen, dass der MQTT-Client erfolgreich erstellt wurde.

    Das Hauptprogramm beginnt mit einer Endlosschleife (while True), in der der Zustand
    des Tasters überwacht wird.

    Wenn der Taster gedrückt wird (der Tasterwert ist 0), wird der MQTT-Client verbunden
    und eine Verbindung zum MQTT-Broker hergestellt.

    Eine MQTT-Nachricht mit dem Text "Taster A on" wird an das MQTT-Topic "TasterA" gesendet.

    Die LED blinkt dreimal auf, um anzuzeigen, dass die MQTT-Nachricht erfolgreich
    publiziert wurde.

    Der MQTT-Client wird getrennt.

    Das Programm wartet für 0,5 Sekunden, bevor es den Tasterstatus erneut überprüft.

    Wenn der Taster nicht gedrückt wird (der Tasterwert ist 1), wird eine kurze Verzögerung
    von 0,1 Sekunden eingefügt, bevor das Programm den Tasterstatus erneut überprüft.

Das Programm überwacht also kontinuierlich den Zustand des Tasters und sendet
über MQTT eine entsprechende Meldung, wenn der Taster gedrückt wird.
Der Status der Verbindung und des Publizierens wird mit Hilfe der LED-Anzeige angezeigt.
"""
