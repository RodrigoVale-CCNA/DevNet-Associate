# Lab: Parse JSON Data with Python

## Introduction

In this lab, you will harness the capabilities of Python to parse data structured in JSON format. JSON, standing for JavaScript Object Notation, is a lightweight and popular format for data interchange. Often when web applications communicate with APIs or back-end services, JSON is the data format of choice.

Throughout this lab, we'll guide you through Python code samples, focusing on parsing the provided JSON data.

## Objective

- Parse JSON data in Python

## Prerequisites

- Python environment setup
- Familiarity with basic Python programming

## Part 1: Parse JSON in Python

JSON provides a structured and straightforward way to represent data. Python comes with built-in tools that make reading and parsing JSON data a breeze.

### 1. Prepare the JSON Data

Use the JSON content generated from the previous lab, which represents the configuration details of two routers. The file should be saved as `network_config.json`.

### 2. Write a Python Script to Parse the JSON Data

Create a Python script named `parse_json.py`.

1. **Setup the Script**: Start by importing the required library:

```python
import json
```

2. **Load the JSON File**: Read the JSON content from the file:

```python
with open('network_config.json', 'r') as file:
    data = json.load(file)
```

3. **Extract Data**: For our example, let's extract the IP addresses and their associated interface names for both routers:

```python
for router in data['routers']:
    router_name = router['hostname']
    for interface in router['interfaces']:
        iface_name = interface['name']
        ip = interface['ip_address']
        print(f"{router_name}, Interface {iface_name} has IP: {ip}")
```

4. **Execute the Script**: Now, run the script to view the parsed data.

```bash
python parse_json.py
```

After executing, you should see the extracted IP addresses and their associated interface names displayed.

## Conclusion

By completing this lab, you've honed your skills in parsing JSON data using Python. You've seen how to structure your code, load JSON content, and traverse the JSON tree structure to extract relevant information. As JSON is one of the primary data formats in modern web development, mastering these skills is essential for various applications and services.