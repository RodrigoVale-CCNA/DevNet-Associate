#importando a bibliotecas
import requests

#Desabilitando os warnings
requests.packages.urllib3.disable_warnings()

#Detalhes da conexão
HOST = 'devnetsandboxiosxe.cisco.com'
USER = 'admin'
PASS = 'C1sco12345'
TARGET_INTERFACE = 'Loopback213' # Interface específica a ser consultada

def main():
    """Recupera os detalhes de uma interface específica em um dispositivo Cisco IOS-XE"""
    
    # RESTCONF URL para a interface específica
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces/interface={TARGET_INTERFACE}"
    

    # RESTCONF headers
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }

    # realiza a requisição GET
    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
    

    # Imprime a resposta
    print(response.text)
    
# Chamada da função main
if __name__ == '__main__':
    main()
