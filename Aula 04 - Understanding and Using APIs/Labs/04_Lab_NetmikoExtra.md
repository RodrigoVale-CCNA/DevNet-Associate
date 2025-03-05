# Lab 4: Verifying the Creation of a Network Interface using Netmiko

## Objective:

Building upon Lab 2 and Lab 3, in this exercise, we'll use Netmiko to verify whether a specific interface has been created on a Cisco device. The script will check for the presence of the loopback interface created in Lab 3 and output the relevant details or a notification message if not found.

## Prerequisites:

1. Completion of Lab 2: *Processing Cisco Device Output using Netmiko* and Lab 3: *Creating a Network Interface using Netmiko*.
2. A Python environment with the `netmiko` library installed.

### Steps:

1. **Set up Your Python Environment**

Ensure `netmiko` is installed:

```bash
pip install netmiko
```

2. **Write the Python Script**

Firstly, we'll set up the device details and establish a connection:

```python
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': 'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876',
    'port': 22,
    'secret': '',
    'verbose': False
}

# Create a connection
connection = ConnectHandler(**device)

# Fetch interface details
output = connection.send_command('show ip int brief', use_textfsm=True)

# Close the connection
connection.disconnect()
```

Now, let's search for the specific interface and display relevant details:

```python
# Target loopback interface from Lab 3
target_interface = "Loopback213"

interface_found = False

for entry in output:
    if entry['intf'] == target_interface:
        interface_found = True
        print(f"Interface Name: {entry['intf']}")
        print(f"IP Address: {entry['ipaddr']}")
        print(f"Status: {entry['status']}")
        print(f"Protocol: {entry['proto']}")
        break

if not interface_found:
    print(f"Interface {target_interface} not found on the device.")
```

3. **Save and Execute the Script**

After saving your Python script, run it. The script will provide either the details of the loopback interface from Lab 3 or a notification message if the interface is not found.

## Conclusion:

In Lab 4, we demonstrated how to use Netmiko to verify specific configurations on a Cisco device. This method can be extended to validate any type of configuration, ensuring consistency and accuracy in network setups.