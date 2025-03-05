# Lab 1: Connect to a Cisco Device using Netmiko and Retrieve Command Output

## Objective:

In this lab, you will use Python along with the Netmiko library to connect to a Cisco device. You will then retrieve and print the output of the `show ip int brief` command.

## Requirements:

- Python installed
- Netmiko library installed (`pip install netmiko`)

### Steps:

1. **Setting up the Environment**
    - Before you start, make sure you have Python installed on your machine.
    - Install Netmiko library using pip:
        ```bash
        pip install netmiko
        ```

2. **Writing the Python Script**
    - Create a new Python file named `netmiko_cisco_lab.py`.
    - Use the following template to write the script:

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
    output = connection.send_command('show ip int brief')

    # Close the connection
    connection.disconnect()

    # Print the output
    print(output)
    ```

3. **Execute the Script**
    - Run the script:
    ```bash
    python netmiko_cisco_lab.py
    ```

    - Observe the output of the `show ip int brief` command on your terminal.

### Conclusion:
By completing this lab, you've successfully connected to a Cisco device using the Netmiko library and executed a command programmatically, retrieving its output. You can expand on this script by adding more commands or processing the output further as per your requirements.