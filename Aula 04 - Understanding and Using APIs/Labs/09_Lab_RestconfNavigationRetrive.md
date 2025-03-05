# Lab 9: Navigating and Retrieving Interface Details via RESTCONF

## Objective:

In this lab, we'll dive deeper into the power of RESTCONF by making individual requests for each property of an interface on a Cisco device. Instead of fetching all details in a single request, we'll navigate through the RESTCONF data tree, property by property.

## Prerequisites:

1. Completion of previous labs, particularly Lab 7 and Lab 8.
2. A Python environment with the `requests` library installed.
3. Access to a Cisco device with RESTCONF support.

### Steps:

1. **Set up Your Python Environment**

If you haven't already installed the `requests` library, do so using pip:

```bash
pip install requests
```

2. **Write the Python Script**

Here's the full code to navigate and retrieve interface details via RESTCONF:

```python
import requests

# Disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Device details and target interface
HOST = 'sandbox-iosxe-recomm-1.cisco.com'
USER = 'developer'
PASS = 'lastorangerestoreball8876'
TARGET_INTERFACE = "Loopback213"

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
```

3. **Save and Execute the Script**

Save your Python script, and then run it. You'll see individual properties of the specified interface printed to the console.

## Conclusion:

In Lab 9, we saw the granularity RESTCONF offers by fetching interface properties one at a time. By understanding how the RESTCONF data tree is structured, we can make precise queries, which is especially useful when dealing with large datasets or when we need only specific information.