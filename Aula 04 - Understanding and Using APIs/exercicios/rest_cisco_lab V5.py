#importando a bibliotecas
import requests

#Desabilitando os warnings
requests.packages.urllib3.disable_warnings()

#Detalhes da conexão
HOST = 'devnetsandboxiosxe.cisco.com'
USER = 'admin'
PASS = 'C1sco12345'
TARGET_INTERFACE = 'Loopback213' # Interface específica a ser consultada


#Construindo a URL
TARGET_INTERFACE = "Loopback213"
DESCRIPTION = "Change by RESTCONF"
ENABLED = "true"

def main():
    # Construindo a URL
    payload = f'{{"ietf-interfaces:interface": {{"name": "{TARGET_INTERFACE}", "description": "{DESCRIPTION}", "type": "iana-if-type:softwareLoopback", "enabled": {str(ENABLED).lower()}}}}}'
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces/interface={TARGET_INTERFACE}"
    
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    }

    # Enviar a requisição utilizando o método POST
    response = requests.put(url, auth=(USER, PASS), headers=headers, verify=False, data=payload)
    
    # checando o status code da resposta
    if response.status_code == 204:
        print(f"Status Code: {response.status_code}")
        print("Success: Interface details updated.")
    else:
        print(f"Status Code: {response.status_code}")
        print("Error message returned:")
        print(response.text)

if __name__ == '__main__':
    main()