# Lab: Parse YAML Data with Python

## Introduction

In this lab, you will leverage Python to parse data structured in YAML format. YAML, which stands for "YAML Ain't Markup Language" (a recursive acronym), is a human-readable data serialization format. Due to its clarity and simplicity, it's commonly used for configuration files and data exchange between languages with different data structures.

Throughout this lab, we will delve into Python code samples, focusing on parsing the provided YAML data.

## Objective

- Parse YAML data in Python

## Prerequisites

- Python environment setup
- Basic understanding of Python programming

## Part 1: Parse YAML in Python

YAML is often chosen for its legibility and ease of use. Python has libraries that facilitate YAML parsing, and we'll explore one of the most popular ones: PyYAML.

### 1. Prepare the YAML Data

Utilize the YAML content generated from a previous lab, representing the configuration details of two routers. The content should be saved in a file named `network_config.yaml`.

### 2. Write a Python Script to Parse the YAML Data

Create a Python script named `parse_yaml.py`.

1. **Setup the Script**: Start by importing the necessary library. If you haven't installed the `pyyaml` library yet, you can do so using pip: `pip install pyyaml`.

```python
import yaml
```

2. **Load the YAML File**: Read the YAML content from the file:

```python
with open('network_config.yaml', 'r') as file:
    data = yaml.safe_load(file)
```

3. **Extract Data**: To showcase the parsing, we'll extract the IP addresses and their associated interface names for both routers:

```python
for router in data['routers']:
    router_name = router['hostname']
    for interface in router['interfaces']: 
        iface_name = interface['name']
        ip = interface['ip_address']
        print(f"{router_name}, Interface {iface_name} has IP: {ip}")
```

4. **Execute the Script**: Now, run the script to observe the parsed data.

```bash
python parse_yaml.py
```

Upon execution, you should see the extracted IP addresses and their associated interface names.

## Conclusion

By the end of this lab, you've mastered the art of parsing YAML data using Python. With YAML being a popular choice for configuration and data representation, having the skills to parse and manipulate YAML data proves invaluable in many software development and IT scenarios. Continue practicing, and you'll become proficient in handling a variety of data formats.