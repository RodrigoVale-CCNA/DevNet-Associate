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
output = connection.send_command("show ip int brief", use_textfsm=True)

#Fechando a conexão
connection.disconnect()

#procurando a interface criaada no exercicio anterior
target_interface = "Loopback213"

interface_found = False

#Iterando sobre a saída para encontrar a interface
for entry in output:
    if entry['interface'] == target_interface:
        interface_found = True
        print(f"Interface Name: {entry['interface']}")
        print(f"IP Address: {entry['ip_address']}")
        print(f"Status: {entry['status']}")
        print(f"Protocol: {entry['proto']}")
        break
if not interface_found:
    print(f"Interface {target_interface} not found")

#Delimitador para melhor visualização
print("\n\n\n")


