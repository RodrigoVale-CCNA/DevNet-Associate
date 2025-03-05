# Lab 5: Deleting a Network Interface using Netmiko

## Objective:

In this lab, we'll use Netmiko to delete a specific interface that was created in a previous lab on a Cisco device. After completing this exercise, the interface created in Lab 3 will be removed from the device.

## Prerequisites:

1. Completion of Lab 3: *Creating a Network Interface using Netmiko*.
2. A Python environment with the `netmiko` library installed.

### Steps:

1. **Set up Your Python Environment**

If you haven't already installed `netmiko`, do so using pip:

```bash
pip install netmiko
```

2. **Write the Python Script**

Begin by importing the necessary library and setting up the device and interface details:

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

# Loopback Details
loopback = {"int_name": "Loopback213"}

# CLI configuration to remove the interface
interface_config = [
    f"no interface {loopback['int_name']}"
]
```

Now, establish a connection, send the configuration, and print the output:

```python
# Create a connection
connection = ConnectHandler(**device)

# Send configuration to the device
output = connection.send_config_set(interface_config)

# Close the connection
connection.disconnect()

# Print the output to confirm deletion
print("The following configuration was sent:")
print(output)
```

3. **Save and Execute the Script**

After saving your Python script, run it to delete the target interface.

### Note:
To re-create the interface for future labs or exercises, execute the script from Lab 3: *Creating a Network Interface using Netmiko* again.

## Conclusion:

Lab 5 demonstrated how to use Netmiko to remove specific configurations from a Cisco device. This is especially useful in scenarios where temporary configurations need to be reverted, ensuring a clean and predictable network state.