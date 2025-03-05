#importando a bibliotecas
import requests

#Desabilitando os warnings
requests.packages.urllib3.disable_warnings()

#Detalhes da conexão
HOST = 'devnetsandboxiosxe.cisco.com'
USER = 'admin'
PASS = 'C1sco12345'
TARGET_INTERFACE = 'Loopback213'

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
    interfaces_data = response.json()

    found = False
    for intf in interfaces_data["ietf-interfaces:interfaces"]["interface"]:
        if intf["name"] == TARGET_INTERFACE:
            found = True
            
            ipv4_addresses = intf["ietf-ip:ipv4"].get("address", [])
            ipv6_addresses = intf["ietf-ip:ipv6"].get("address", [])
            
            print(f"Interface: {intf['name']}")
            print(f"Description: {intf['description']}")
            print(f"Type: {intf['type']}")
            print(f"Enabled: {intf['enabled']}")
            
            if ipv4_addresses:
                for address in ipv4_addresses:
                    print(f"IPv4 Address: {address['ip']}")
                    print(f"IPv4 Netmask: {address['netmask']}")
            else:
                print(f"IPv4 Address: Not Configured")
                print(f"IPv4 Netmask: Not Configured")
            
            if ipv6_addresses:
                for address in ipv6_addresses:
                    print(f"IPv6 Address: {address['ip']}")
                    print(f"IPv6 Prefix: {address['prefix-length']}")
            else:
                print(f"IPv6 Address: Not Configured")
                print(f"IPv6 Prefix: Not Configured")
            
    if not found:
        print(f"Interface {TARGET_INTERFACE} not found on the device.")

if __name__ == '__main__':
    main()
