#importando a bibliotecas
import requests

#Desabilitando os warnings
requests.packages.urllib3.disable_warnings()

#Detalhes da conexão
HOST = 'devnetsandboxiosxe.cisco.com'
USER = 'admin'
PASS = 'C1sco12345'
TARGET_INTERFACE = 'Loopback213' # Interface específica a ser consultada

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

def main():
    # Base URL for our target interface
    base_url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces/interface={TARGET_INTERFACE}"
    
    # Check if the interface exists
    response = requests.get(base_url, auth=(USER, PASS), headers=headers, verify=False, timeout=10)
    
    if response.status_code == 200:
        # Fetch interface name
        url = f"{base_url}/name"
        response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False, timeout=10)
        print(f"Interface: {response.json()['ietf-interfaces:name']}")

        # Fetch description
        url = f"{base_url}/description"
        response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False, timeout=10)
        print(f"Description: {response.json().get('ietf-interfaces:description', 'Not Available')}")

        # Fetch type
        url = f"{base_url}/type"
        response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False, timeout=10)
        print(f"Type: {response.json()['ietf-interfaces:type']}")

        # Fetch enable status
        url = f"{base_url}/enabled"
        response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False, timeout=10)
        print(f"Enabled: {response.json()['ietf-interfaces:enabled']}")
        
        # Fetch IPv4 data
        url = f"{base_url}/ietf-ip:ipv4"
        response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False, timeout=10)
        ipv4_data = response.json()
        ipv4_addresses = ipv4_data["ietf-ip:ipv4"].get("address", [])
        
        if ipv4_addresses:
            for addr in ipv4_addresses:
                print(f"IPv4 Address: {addr['ip']}")
                print(f"IPv4 Netmask: {addr['netmask']}")
        else:
            print("IPv4 Address: Not Configured")
            print("IPv4 Netmask: Not Configured")

        # Fetch IPv6 data
        url = f"{base_url}/ietf-ip:ipv6"
        response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False, timeout=10)
        ipv6_data = response.json()
        ipv6_addresses = ipv6_data["ietf-ip:ipv6"].get("address", [])
        
        if ipv6_addresses:
            for addr in ipv6_addresses:
                print(f"IPv6 Address: {addr['ip']}")
                print(f"IPv6 Prefix: {addr['prefix-length']}")
        else:
            print("IPv6 Address: Not Configured")
            print("IPv6 Prefix: Not Configured")

    else:
        print(f"Interface {TARGET_INTERFACE} not found.")

if __name__ == '__main__':
    main()