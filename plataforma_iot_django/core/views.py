from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import DispositivoIoT
# from .mqtt_handler import mqtt_subscribe

def cadastrar_dispositivo(request):
    if request.method == 'POST':
        serialNumber = request.POST['serialNumber']
        dados = request.POST['dados']
        
        # Verifique se os campos são válidos e não estão vazios
        if serialNumber and dados:
            # Crie um novo dispositivo IoT
            dispositivo = DispositivoIoT(serialNumber=serialNumber, dados=dados)
            dispositivo.save()
            return redirect('listar_dispositivos')

    return render(request, 'core/cadastro_dispositivo.html')

def listar_dispositivos(request):
    dispositivos = DispositivoIoT.objects.all()
    return render(request, 'core/listagem_dispositivos.html', {'dispositivos': dispositivos})

# Inicie a assinatura MQTT quando o Django for iniciado
# mqtt_subscribe()