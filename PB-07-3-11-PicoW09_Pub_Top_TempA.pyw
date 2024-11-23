#==========================================================================
#
# PB-07-3-11-PicoW09_Pub_Top_TempA.pyw
#
#  1 Taster (TasterA)
#
#  onboard LED:
#  Z47  *  =  WLAN Verbindung erfolgreich hergestellt
#  Z53  **  =  MQTT-Client erfolgreich erstellt
#  Z61  ***  =  "on" ge-publisht
#
#  Z28  MQTT_TOPIC = "TempA"
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
from machine import ADC
# WLAN-Zugangsdaten und MQTT-Broker-Details
WIFI_SSID = wlanSSID()
WIFI_PASSWORD = wlanPW()
MQTT_BROKER = IP_MQTT_broker()
MQTT_TOPIC = "TempA"

# Initialisieren des Tem-ADCs  und LED-Anzeige
Temperatursensor = ADC(4);Umrechnungsfaktor = 3.3 / (65535)
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
client = MQTTClient("PicoW09", MQTT_BROKER)

Blinki = 2 ;LED_blinkt(Blinki); print("LED_blinkt ", Blinki);sleep(1)
#  **  =  MQTT-Client erfolgreich erstellt

# Hauptprogramm
while True:
    EinlesewertDigi = Temperatursensor.read_u16()
    Spannung = EinlesewertDigi * Umrechnungsfaktor
    temperatur = 27 - (Spannung - 0.706) / 0.001721
    print("Temperatur (°C): ", temperatur)
    TempStr=str(temperatur)
    client.connect()
    client.publish(MQTT_TOPIC, TempStr)
    
    Blinki = 3 ;LED_blinkt(Blinki); print("LED_blinkt ", Blinki);sleep(1)
    #  ***  =  "on" ge-publisht
    client.disconnect()
    sleep(5)
 
        
"""
Dieses Programm ist in der Programmiersprache MicroPython geschrieben und soll
eine Temperaturmessung mit einem Pico-W09 Mikrocontroller durchführen und die
gemessene Temperatur über das MQTT-Protokoll an einen MQTT-Broker senden.
Hier ist eine detaillierte Erläuterung des Programms:

    Zunächst werden die benötigten Bibliotheken importiert:
        machine: Eine Bibliothek, die Funktionen zur Steuerung von Hardwarekomponenten
        bereitstellt.
        network: Eine Bibliothek zur Verbindung mit WLAN-Netzwerken.
        time.sleep: Eine Funktion zum Einbauen von Verzögerungen im Programmablauf.
        simple.MQTTClient: Eine vereinfachte MQTT-Client-Bibliothek.
        Zugang_DC: Eine benutzerdefinierte Bibliothek, die Zugangsdaten für WLAN und den
        MQTT-Broker enthält.
        machine.ADC: Eine Klasse zum Zugriff auf den analogen Eingang des Mikrocontrollers.

    Es werden Variablen definiert, die die WLAN-Zugangsdaten und die MQTT-Broker-Details
    enthalten.

    Der Temperatursensor (ADC) und die LED werden initialisiert. Der ADC wird verwendet,
    um die analoge Spannung des Temperatursensors zu messen, und der Umrechnungsfaktor
    wird berechnet, um die Spannung in einen Temperaturwert umzuwandeln.
    Die LED wird verwendet, um den Status der Verbindung und das Publizieren von
    MQTT-Meldungen anzuzeigen.

    Es wird eine Funktion LED_blinkt(Zahl) definiert, die die LED eine bestimmte Anzahl von
    Malen blinken lässt. Dies dient dazu, den aktuellen Status des Programms anzuzeigen.

    Eine Verbindung zum WLAN wird hergestellt. Die WLAN-Zugangsdaten werden verwendet,
    um sich mit dem WLAN-Netzwerk zu verbinden. Das Programm wartet in einer Schleife,
    bis die Verbindung hergestellt ist.

    Die LED blinkt einmal auf, um anzuzeigen, dass die WLAN-Verbindung erfolgreich
    hergestellt wurde.

    Ein MQTT-Client wird erstellt. Der Client wird mit dem Namen "PicoW09" und den
    MQTT-Broker-Details initialisiert.

    Die LED blinkt zweimal auf, um anzuzeigen, dass der MQTT-Client erfolgreich erstellt wurde.

    Das Hauptprogramm beginnt mit einer Endlosschleife (while True), in der die Temperatur
    gemessen und an den MQTT-Broker gesendet wird.

    Der Analog-Digital-Konverter (ADC) des Temperatursensors wird ausgelesen, um den
    aktuellen Wert der analogen Spannung zu erhalten.

    Die Spannung wird mit dem Umrechnungsfaktor multipliziert, um die Temperatur in
    Grad Celsius zu berechnen. Die spezifische Umrechnungsformel wird verwendet,
    um den Temperaturwert basierend auf dem gemessenen Spannungswert zu berechnen.

    Der Temperaturwert wird auf der Konsole ausgegeben.

    Der MQTT-Client wird verbunden und eine Verbindung zum MQTT-Broker hergestellt.

    Der Temperaturwert wird in einen String konvertiert.

    Der Temperaturwert wird über den MQTT-Client und das MQTT-Protokoll an das
    MQTT-Topic "TempA" gesendet.

    Die LED blinkt dreimal auf, um anzuzeigen, dass die MQTT-Nachricht erfolgreich publiziert wurde.

    Der MQTT-Client wird getrennt.

    Das Programm wartet für 5 Sekunden, bevor es den Messzyklus erneut startet.

Das Programm führt also kontinuierlich Temperaturmessungen durch, sendet die
gemessenen Werte über MQTT und gibt den Status der Verbindung und des Publizierens
mit Hilfe der LED-Anzeige aus.
"""
