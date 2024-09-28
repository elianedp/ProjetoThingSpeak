import network
import time
import urequests
def conecta(ssid, senha):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station
ssid = "Junior"
senha = "euamopalmeiras"
station = conecta(ssid, senha)

if station.isconnected():
    print("conectado ao wi-fi")
    print("Acessando o site...")
    response = urequests.get("http://example.com")
    print("Página acessada:")
    print(response.text)
else:
    print("não foi possível conectar wi-fi")
    
    
                               