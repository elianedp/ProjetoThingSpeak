from wifi_lib import conecta
ssid = "Junior"
senha = "euamopalmeiras"
station = conecta(ssid, senha)
if station.isconnected():
    print("Conectado ao Wi-Fi")
    print("acessando site")
    import urequests
    response = urequests.get("http://example.com")
    print("pagina acessada")
    
    print(response.text)
else:
    prin("não foi possível conectar wifi")
    
