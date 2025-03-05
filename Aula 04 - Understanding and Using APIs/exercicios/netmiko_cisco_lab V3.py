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
    "description": "Demo interface by python and netmiko",
    "ip": "192.168.213.213",
    "netmask": "255.255.255.255"
}
# Lista de comandos para configuração da interface loopback
interface_config = [
    f"interface {loopback['interface']}",
    f"description {loopback['description']}", 
    f"ip address {loopback['ip']} {loopback['netmask']}",
    "no shutdown"
]


# Abrindo conexão com o dispositivo
connection = ConnectHandler(**device)

#EXEMPLO DE COMANDOS
#command = 'show ip int brief'
#command = 'show run'
output = connection.send_config_set(interface_config)

#Fechando a conexão
connection.disconnect()

#Imprimindo a saída
print("Configuração aplicada com sucesso!")
print(output)

