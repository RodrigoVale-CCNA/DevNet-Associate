# Lab 2: Processing Cisco Device Output using Netmiko

## Objective:

In this lab, we'll build upon our previous exercise and introduce the use of TextFSM, integrated within Netmiko, to structure the output from a Cisco device. This will allow us to work with structured data, making further processing or analysis significantly easier.

## Prerequisites:

1. Completion of Lab 1: *Connect to a Cisco Device using Netmiko and Retrieve Command Output*.
2. A Python environment with the `netmiko` library installed.

### Steps:

1. **Set up Your Python Environment**

If you haven't already installed `netmiko`, do so using pip:

```bash
pip install netmiko
```

2. **Write the Python Script**

Start by importing the required library:

```python
from netmiko import ConnectHandler

# Device details
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

# Execute command and retrieve output
output = connection.send_command('show ip int brief', use_textfsm=True)

# Close the connection
connection.disconnect()

# Print the output
print(output)

# Print each entry in output
for entry in output:
    print(entry)
```

3. **Save and Execute the Script**

Save your Python script and then run it. The output will provide structured data from your Cisco device based on the `show ip int brief` command.

## Conclusion:

In this lab, we demonstrated how to efficiently use Netmiko's integrated TextFSM feature to retrieve and structure command outputs from Cisco devices. This provides a powerful foundation for further network automation tasks and integrations.