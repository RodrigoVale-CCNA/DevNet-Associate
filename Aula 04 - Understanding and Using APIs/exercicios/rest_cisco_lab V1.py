#importando a bibliotecas
import requests

#Desabilitando os warnings
requests.packages.urllib3.disable_warnings()

#Detalhes da conexão
HOST = 'devnetsandboxiosxe.cisco.com'
USER = 'admin'
PASS = 'C1sco12345'

def main():
    #Recuperando detalhes da interface do dispositivo via RESTCONF


    #contruindo a URL
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"

    #Headers
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }
    #Realizando a requisição GET
    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)

    #Imprimindo a resposta
    print(response.text)

if __name__ == '__main__':
    main()
