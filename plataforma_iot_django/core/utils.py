# core/utils.py
from .models import DispositivoIoT  # Importe os modelos necessários

def processar_mensagem_mqtt(serial_number, dados):
    try:
        # Verifique se o dispositivo já existe no banco de dados
        dispositivo, created = DispositivoIoT.objects.get_or_create(
            serialNumber=serial_number
        )

        # Converta o valor recebido para float
        novo_valor = float(dados['channelValue'])
        
        # Converta o valor existente no banco de dados para float
        valor_existente = float(dispositivo.dados.get('channelValue'))
        print("valor_existente:", valor_existente)

        # Verifique se o novo valor é maior que o valor existente no banco de dados
        if novo_valor < valor_existente:
            # Atualize o JSON com o campo 'erro'
            dados['erro'] = 'numero maior'

        # Atualize os dados do dispositivo
        dispositivo.dados = dados
        dispositivo.save()

        print(f"Dispositivo {serial_number} atualizado com dados: {dados}")
    except Exception as e:
        print("Erro ao processar a mensagem MQTT:", str(e))
