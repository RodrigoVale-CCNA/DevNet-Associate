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

# Abrindo conexão com o dispositivo
connection = ConnectHandler(**device)

#EXEMPLO DE COMANDOS
#command = 'show ip int brief'
#command = 'show run'
output = connection.send_command('show ip int brief')

#Fechando a conexão
connection.disconnect()

#Imprimindo a saída
print(output)

