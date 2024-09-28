import network
import time
import dht
import machine
import urequests

# Função para conectar ao Wi-Fi
def conecta(ssid, senha):
    # Configura a interface de rede Wi-Fi no modo estação (STA_IF)
    station = network.WLAN(network.STA_IF)
    station.active(True)  # Ativa a interface Wi-Fi
    station.connect(ssid, senha)  # Conecta ao Wi-Fi com o SSID e senha fornecidos
    # Tenta conectar ao Wi-Fi por até 50 tentativas
    for t in range(50):
        if station.isconnected():  # Verifica se a conexão foi bem-sucedida
            print("Conectado ao Wi-Fi")
            break  # Sai do loop se a conexão for estabelecida
        time.sleep(0.1)  # Aguarda 100ms antes de tentar novamente
    else:
        # Se após 50 tentativas a conexão falhar, exibe uma mensagem
        print("Falha na conexão Wi-Fi")
        return station
    return station  # Retorna o objeto de conexão Wi-Fi

# Função para coletar dados do sensor DHT11 (temperatura e umidade)
def coleta_dados():
    sensor = dht.DHT11(machine.Pin(4))  # Inicializa o sensor DHT11 no pino 4
    sensor.measure()  # Mede temperatura e umidade
    temperatura = sensor.temperature()  # Obtém a temperatura em Celsius
    umidade = sensor.humidity()  # Obtém a umidade relativa (%)
    return temperatura, umidade  # Retorna os valores de temperatura e umidade

# Função para enviar os dados coletados ao ThingSpeak
def envia_para_thingspeak(temperatura, umidade):
    api_key = '637ET1DA9Y7W7YZV'  # A sua chave de API do ThingSpeak
    # Monta a URL com os dados de temperatura e umidade para enviar ao ThingSpeak
    url = "http://api.thingspeak.com/update?api_key=" + api_key + \
          "&field1=" + str(temperatura) + "&field2=" + str(umidade)
    resposta = urequests.get(url)  # Faz uma requisição GET para enviar os dados
    print("Resposta do ThingSpeak:", resposta.text)  # Exibe a resposta do servidor

# Configurações de SSID (nome da rede) e senha do Wi-Fi
ssid = 'Junior'  # Substitua pelo nome da sua rede Wi-Fi
senha = 'euamopalmeiras'  # Substitua pela sua senha do Wi-Fi
station = conecta(ssid, senha)  # Tenta conectar ao Wi-Fi com o SSID e senha fornecidos

# Loop infinito para coletar e enviar os dados periodicamente
while True:
    if station.isconnected():  # Verifica se ainda está conectado ao Wi-Fi
        temperatura, umidade = coleta_dados()  # Coleta os dados do sensor
        print("Temperatura:", temperatura, "°C")  # Exibe a temperatura no terminal
        print("Umidade:", umidade, "%")  # Exibe a umidade no terminal
        envia_para_thingspeak(temperatura, umidade)  # Envia os dados para o ThingSpeak
        time.sleep(15)  # Aguarda 15 segundos antes de coletar e enviar novos dados
    else:
        print("Sem conexão Wi-Fi")  # Mensagem de erro caso a conexão Wi-Fi seja perdida
        time.sleep(15)  # Tenta reconectar após 15 segundos

