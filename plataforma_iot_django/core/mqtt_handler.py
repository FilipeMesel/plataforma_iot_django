import os
import sys

# Adicione o diretório raiz do seu projeto Django ao sys.path
django_project_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(django_project_directory))

# Configurar as configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plataforma_iot_django.settings")  # Use o caminho correto para suas configurações Django

import django
django.setup()

# Resto do seu código MQTT


import django
django.setup()

# Agora você pode importar os módulos do Django sem erros de configuração
from core.utils import processar_mensagem_mqtt  # Importe a função do seu aplicativo Django
import paho.mqtt.client as mqtt
import json

# Resto do seu código MQTT

def on_connect(client, userdata, flags, rc):
    print("Conectado com o código de resultado: " + str(rc))
    client.subscribe("F4CFA2958F30/pub")

def on_message(client, userdata, msg):
    print("Mensagem recebida no tópico " + msg.topic)
    try:
        data = json.loads(msg.payload.decode())
        serial_number = data.get('deviceId')
        dados = data.get('channels')[1]

        print(dados.get('channelId'))
        if dados.get('channelId') == "di06":
            if serial_number and dados:
                # Importe a função diretamente do módulo
                from core.utils import processar_mensagem_mqtt

                # Chame a função do aplicativo Django para processar a mensagem
                processar_mensagem_mqtt(serial_number, dados)
    except Exception as e:
        print("Erro ao processar a mensagem MQTT:", str(e))

def connect_and_subscribe():
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    # Configure as credenciais (nome de usuário e senha) se necessário
    client.username_pw_set("monitron", "monitron")
    client.connect("mqttmonitron.jelastic.saveincloud.net", 1883, 60)

    client.loop_forever()

if __name__ == "__main__":
    connect_and_subscribe()
