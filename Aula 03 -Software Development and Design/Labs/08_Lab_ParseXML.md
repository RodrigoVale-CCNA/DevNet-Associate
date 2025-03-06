# Lab: Parse Different Data Types with Python

## Introduction

In this lab, you will utilize Python to parse XML, a popular data interchange format. Parsing means analyzing a message, dissecting it into its component parts, and understanding the context of each part. When data is transferred between systems, they're often formatted as XML. Before this data can be interpreted and acted upon, it must be parsed into a structured data format.

We will walk through Python code examples, specifically focusing on parsing the provided XML data.

## Objective

- Parse XML data in Python

## Prerequisites

- Python environment setup
- Knowledge of basic Python programming

## Parse XML in Python

XML provides a structured way to represent data. Parsing XML can sometimes require understanding its hierarchy and attributes. Python provides libraries to make this task easier.

### 1. Prepare the XML Data

Use the following XML content, representing a network configuration with details about two routers:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<network>
  <router>
    <id>R1</id>
    <hostname>Router1</hostname>
    <interfaces>
      <interface>
        <name>eth0</name>
        <ip_address>192.168.1.1</ip_address>
        <subnet_mask>255.255.255.0</subnet_mask>
      </interface>
      <interface>
        <name>eth1</name>
        <ip_address>192.168.2.1</ip_address>
        <subnet_mask>255.255.255.0</subnet_mask>
      </interface>
    </interfaces>
  </router>
  <router>
    <id>R2</id>
    <hostname>Router2</hostname>
    <interfaces>
      <interface>
        <name>eth0</name>
        <ip_address>192.168.3.1</ip_address>
        <subnet_mask>255.255.255.0</subnet_mask>
      </interface>
      <interface>
        <name>eth1</name>
        <ip_address>192.168.4.1</ip_address>
        <subnet_mask>255.255.255.0</subnet_mask>
      </interface>
    </interfaces>
  </router>
</network>
```

Save this content to a file named `network_config.xml`.

### 2. Write a Python Script to Parse the XML Data

Create a Python script named `parse_xml.py`.

1. **Setup the Script**: Begin by importing the necessary library:

```python
import xml.etree.ElementTree as ET
```

2. **Parse the XML File**: Parse the XML content:

```python
tree = ET.parse('network_config.xml')
root = tree.getroot()
```

3. **Extract Data**: For our example, extract the IP addresses and associated interface names for both routers:

```python
for router in root.findall('router'):
    router_name = router.find('hostname').text
    for interface in router.find('interfaces').findall('interface'):
        iface_name = interface.find('name').text
        ip = interface.find('ip_address').text
        print(f"{router_name}, Interface {iface_name} has IP: {ip}")
```

4. **Execute the Script**: Run the script to see the parsed data.

```bash
python parse_xml.py
```

You should observe the extracted IP addresses and their associated interface names being printed.

## Conclusion

By the end of this lab, you've gained experience in parsing XML data using Python, understanding the structure of the XML and extracting relevant information.