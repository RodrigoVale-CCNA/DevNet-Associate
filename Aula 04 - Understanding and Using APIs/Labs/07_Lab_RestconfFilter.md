# Lab 7: Using RESTCONF with Python to Retrieve and Validate Interface Details

## Objective:

In this lab, we'll leverage the RESTCONF protocol to communicate with a Cisco device. We'll retrieve interface details and validate the presence of a specific interface. We will also ensure that the response is structured and that multiple IPv4 or IPv6 addresses are handled accordingly.

## Prerequisites:

1. Understanding of previous labs, especially Lab 6 where we connected using Netmiko.
2. A Python environment with the `requests` library installed.

### Steps:

1. **Set up Your Python Environment**

If you haven't already installed `requests`, do so using pip:

```bash
pip install requests
```

2. **Write the Python Script**

Start by importing the necessary libraries and setting up your device credentials:

```python
import requests

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Device and login details
HOST = 'sandbox-iosxe-recomm-1.cisco.com'
USER = 'developer'
PASS = 'lastorangerestoreball8876'
TARGET_INTERFACE = "Loopback213"

def main():
    """Retrieve Interface details from the device via RESTCONF and check for a specific interface."""
    
    # RESTCONF URL to get interface details
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"

    # RESTCONF headers
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }

    # Perform GET request to retrieve interface details
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
```

3. **Save and Execute the Script**

Save your Python script and then run it. If the interface is present on the device, its details will be printed. If not, a message indicating that the interface was not found will be displayed.

## Conclusion:

In Lab 7, we utilized the RESTCONF protocol with Python to connect to a Cisco device. We retrieved structured interface information and showcased how to validate the presence of a specific interface and display its details.