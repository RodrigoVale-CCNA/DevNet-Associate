# Lab 3: Creating a Network Interface using Netmiko

## Objective:

In this lab, we'll build upon our previous exercises and demonstrate how to create a new network interface on a Cisco device using Netmiko. This allows for automation in network configuration tasks.

## Prerequisites:

1. Completion of Lab 2: *Processing Cisco Device Output using Netmiko*.
2. A Python environment with the `netmiko` library installed.
3. Familiarity with basic Cisco CLI commands.

### Steps:

1. **Set up Your Python Environment**

If you haven't already installed `netmiko`, do so using pip:

```bash
pip install netmiko
```

2. **Write the Python Script**

Start by importing the required library and defining the new loopback interface details:

```python
# Import libraries
from netmiko import ConnectHandler

# New Loopback Details
loopback = {
    "int_name": "Loopback213",
    "description": "Demo interface by Python and netmiko",
    "ip": "192.168.21.3",
    "netmask": "255.255.255.0"
}

# Create a CLI configuration
interface_config = [
    f"interface {loopback['int_name']}",
    f"description {loopback['description']}",
    f"ip address {loopback['ip']} {loopback['netmask']}",
    "no shut"
]

device = {
    'device_type': 'cisco_ios',
    'ip': 'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876',
    'port': 22,          # Default SSH port
    'secret': '',        # Optional, in case of enable password
    'verbose': False     # Optional, set to True for verbose logs
}

# Create a connection
connection = ConnectHandler(**device)

# Send configuration to device
output = connection.send_config_set(interface_config)

# Close the connection
connection.disconnect()

# Print the output to verify the interface configuration
print("The following configuration was sent: ")
print(output)
```

3. **Save and Execute the Script**

Save your Python script and run it. After executing the script, you'll have added a new loopback interface on your Cisco device with the specified details.

## Conclusion:

In this lab, we showcased how Netmiko can be employed to automate configuration tasks on Cisco devices. This kind of automation can significantly improve efficiency in managing network configurations.