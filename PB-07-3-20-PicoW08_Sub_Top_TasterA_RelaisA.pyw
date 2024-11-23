#==========================================================================
#
# PB-07-3-20-PicoW08_Sub_Top_TasterA_RelaisA_Kom.pyw
#
#  1 LED (Relais) 
#
#  onboard LED:
#  Z47  *  =  WLAN Verbindung erfolgreich hergestellt
#  Z53  **  =  MQTT-Client erfolgreich erstellt
#  Z69  ***  =  mit MQTT verbunden und warten im Hauptprogramm
#
#  Z28  MQTT_TOPIC = "TasterA"
#  Z50  client = MQTTClient("PicoW21", MQTT_BROKER)
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
MQTT_TOPIC = "LEDA"

# Initialisieren des Relais-Pins
relay1 = machine.Pin(14, machine.Pin.OUT)
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
client = MQTTClient("PicoW08", MQTT_BROKER)

Blinki = 2 ;LED_blinkt(Blinki); print("LED_blinkt ", Blinki);sleep(1)
#  **  =  MQTT-Client erfolgreich erstellt


# Funktion zum Umschalten des Relais
def toggle_relay(topic, msg):
    if msg == b"1":
        relay1.value(1)
    elif msg == b"0":
        relay1.value(0)


# MQTT-Abonnent erstellen und verbinden
client.set_callback(toggle_relay)
client.connect()
client.subscribe(MQTT_TOPIC)

Blinki = 3 ;LED_blinkt(Blinki); print("LED_blinkt ", Blinki);sleep(1)
 #  ***  =  mit MQTT verbunden und warten im Hauptprogramm

# Hauptprogramm - auf Nachrichten warten
while True:
    client.wait_msg()
    
"""
Das vorliegende Programm ist ein Beispiel für ein MicroPython-Skript, das auf einem ESP8266-Mikrocontroller (wie dem NodeMCU) ausgeführt wird. Das Skript stellt eine Verbindung zu einem WLAN-Netzwerk her und abonniert ein MQTT-Topic, um Nachrichten zu empfangen und das Relais basierend auf den empfangenen Nachrichten zu steuern.

Hier ist eine detaillierte Beschreibung des Programms:

    Importieren der benötigten Module:
        machine: Ein Modul zur Steuerung der Hardware des Mikrocontrollers.
        network: Ein Modul zur Verbindung mit WLAN-Netzwerken.
        time.sleep: Eine Funktion zum Hinzufügen von Zeitverzögerungen.
        simple.MQTTClient: Eine vereinfachte MQTT-Client-Implementierung für MicroPython.

    Importieren der Zugangsdaten und Konfigurationsdetails:
        Die Zugangsdaten für das WLAN (SSID und Passwort) werden aus einer externen Datei namens "Zugang.py" importiert. Dies ist sinnvoll, um sensible Informationen von dem Hauptskript zu trennen.
        Die IP-Adresse des MQTT-Brokers wird ebenfalls aus der "Zugang.py"-Datei importiert.

    Initialisieren des Relais-Pins und der LED:
        Der Pin 14 wird als Ausgang (OUTPUT) konfiguriert und für das Relais verwendet.
        Ein weiterer Pin namens "LED" (vermutlich ein interner LED-Pin des ESP8266) wird ebenfalls als Ausgang konfiguriert und für eine LED verwendet.

    Definieren einer Funktion LED_blinkt(Zahl):
        Diese Funktion lässt die LED eine bestimmte Anzahl von Malen blinken, um den Programmstatus anzuzeigen.
        Die übergebene Zahl gibt an, wie oft die LED blinken soll.

    Herstellen der Verbindung zum WLAN:
        Das WLAN wird aktiviert und eine Verbindung mit den angegebenen Zugangsdaten hergestellt.
        Der Code wartet, bis eine erfolgreiche WLAN-Verbindung hergestellt ist.

    Blinken der LED einmal (LED_blinkt(1)) zur Anzeige einer erfolgreichen WLAN-Verbindung.

    Erstellen des MQTT-Clients:
        Ein MQTT-Client mit dem Namen "PicoW08" wird erstellt und mit dem angegebenen MQTT-Broker verbunden.

    Blinken der LED zweimal (LED_blinkt(2)) zur Anzeige eines erfolgreichen MQTT-Client-Erstellens.

    Definieren einer Funktion toggle_relay(topic, msg):
        Diese Funktion wird aufgerufen, wenn eine MQTT-Nachricht empfangen wird.
        Sie überprüft den Inhalt der Nachricht und schaltet das Relais basierend auf dem empfangenen Wert ein oder aus.

    Konfigurieren des MQTT-Abonnements:
        Die toggle_relay-Funktion wird als Callback-Funktion für den MQTT-Client festgelegt.
        Der MQTT-Client abonniert das angegebene MQTT-Topic.

    Blinken der LED dreimal (LED_blinkt(3)) zur Anzeige einer erfolgreichen Verbindung mit dem MQTT-Broker.

    Hauptprogramm:
        Das Programm befindet sich in einer Endlosschleife (while True), in der es auf dem Eintreffen von MQTT-Nachrichten wartet (client.wait_msg()).
- Sobald eine Nachricht empfangen wird, ruft der MQTT-Client die toggle_relay-Funktion auf, die das Relais entsprechend der empfangenen Nachricht ein- oder ausschaltet.
- Das Programm bleibt in der Schleife und wartet weiterhin auf neue MQTT-Nachrichten.

Das Programm verwendet die Zugangsdaten aus der "Zugang.py"-Datei, um eine Verbindung zum WLAN herzustellen und sich mit einem MQTT-Broker zu verbinden. Es abonniert das angegebene MQTT-Topic und führt die entsprechende Aktion (Einschalten oder Ausschalten des Relais) basierend auf den empfangenen MQTT-Nachrichten aus. Die LED wird verwendet, um den Status der WLAN-Verbindung, des MQTT-Clients und die Verarbeitung von MQTT-Nachrichten anzuzeigen.

Es ist anzumerken, dass die fehlenden Details wie der Inhalt der "Zugang.py"-Datei, der genaue Verwendungszweck des Relais und weitere Implementierungsdetails nicht aus dem gegebenen Code ersichtlich sind. Die Beschreibung basiert auf den vorhandenen Informationen und kann je nach spezifischer Anwendung und Konfiguration variieren.
"""
