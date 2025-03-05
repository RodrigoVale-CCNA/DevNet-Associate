#Importando bibliotecas
from netmiko import ConnectHandler

# Criação de dicionário com as informações de conexão
device = {
    'device_type': 'cisco_ios',
    'ip':'192.168.18.134', #IP do dispositivo dentro de EVE-NG(LOCAL)
    'username':'devpython', #Usuário SSH criado localmente  
    'password':'Python123!',#Senha do usuário SSH
    'port':22, #Default SSH port
    #'secret':'Python123!' #Senha de enable se necessário
}

# Dicionário com as informações de interface loopback
loopback = {
    "interface": "Loopback213",
}
# Lista de comandos para configuração da interface loopback
interface_config = [
    f"no interface {loopback['interface']}",
 ]

# Abrindo conexão com o dispositivo
connection = ConnectHandler(**device)

#EXEMPLO DE COMANDOS
#command = 'show ip int brief'
#command = 'show run'
output = connection.send_config_set(interface_config)

#Fechando a conexão
connection.disconnect()

print(output)
print("A interface Loopback213 foi deletada com sucesso")

#FIM