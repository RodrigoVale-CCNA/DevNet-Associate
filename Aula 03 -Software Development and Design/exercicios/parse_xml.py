#Importando a biblioteca ElementTree
import xml.etree.ElementTree as ET

#Lendo o arquivo XML e armazenando na variável tree
tree = ET.parse('network_config.xml')

#Obtendo o elemento raiz do XML
root = tree.getroot()


#Iterando sobre os elementos do XML
for router in root.findall('router'):
    #Obtendo o nome do roteador
    router_name = router.find('hostname').text
    #Iterando sobre as interfaces do roteador
    for interface in router.find('interfaces').findall('interface'):
        #Obtendo o nome da interface e o IP
        iface_name = interface.find('name').text
        #Obtendo o IP da interface
        ip = interface.find('ip_address').text
        #Imprimindo as informações
        print(f"{router_name}, Interface {iface_name} has IP: {ip}")