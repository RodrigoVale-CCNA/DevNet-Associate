# Lab 10: Updating Interface Details using RESTCONF

## Objective:

In this lab, we will update the description of an existing interface using RESTCONF. This will be an evolutionary lab where we first encounter errors and then resolve them step-by-step to demonstrate the nuances of RESTCONF operations.

## Prerequisites:

1. Completion of previous labs.
2. A Python environment with the `requests` library installed.
3. Access to a Cisco device with RESTCONF support.

### Steps:

1. **Set up Your Python Environment**

If you haven't already installed the `requests` library, do so using pip:

```bash
pip install requests
```

2. **Initial Code with POST**

Start by writing the initial code that uses the HTTP POST method:

```python
import requests

# Disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Device details
HOST = 'sandbox-iosxe-recomm-1.cisco.com'
USER = 'developer'
PASS = 'lastorangerestoreball8876'

# Interface to update
TARGET_INTERFACE = "Loopback213"
DESCRIPTION = "Change by RESTCONF"
ENABLED = True

def main():
    # Constructing the payload
    payload = f'{{"ietf-interfaces:interface": {{"name": "{TARGET_INTERFACE}", "description": "{DESCRIPTION}", "enabled": {ENABLED}}}}}'
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces/interface={TARGET_INTERFACE}"
    
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    }

    # Using POST method
    response = requests.POST(url, auth=(USER, PASS), headers=headers, verify=False, data=payload)
    
    # Check response
    if response.status_code == 204:
        print(f"Status Code: {response.status_code}")
        print("Success: Interface details updated.")
    else:
        print(f"Status Code: {response.status_code}")
        print("Error message returned:")
        print(response.text)

if __name__ == '__main__':
    main()
```

Run the above code. You will encounter an error due to a bad JSON character.

3. **Resolving Error 1: Correcting Boolean Value in JSON Payload**

In JSON, the boolean value `true` should be in lowercase. Adjust the `ENABLED` value in the payload:

Change:
```python
ENABLED = True
```

To:
```python
ENABLED = "true"
```

You can also use Python's `str` method to convert the boolean to a lowercase string value:

Change:
```python
payload = f'{{"ietf-interfaces:interface": {{"name": "{TARGET_INTERFACE}", "description": "{DESCRIPTION}", "enabled": {ENABLED}}}}}'
```

To:
```python
payload = f'{{"ietf-interfaces:interface": {{"name": "{TARGET_INTERFACE}", "description": "{DESCRIPTION}", "enabled": {str(ENABLED).lower()}}}}}'
```

Run the above code. You will encounter an error because we're trying to create an already existing interface using POST.

4. **Resolving Error 2: Change POST to PUT**

Update the HTTP method from POST to PUT:

Change this lines:

```python
# Using POST method
response = requests.post(url, auth=(USER, PASS), headers=headers, verify=False, data=payload)
```

To:

```python
# Using PUT method
response = requests.put(url, auth=(USER, PASS), headers=headers, verify=False, data=payload)
```

5. **Resolving Error 3: Add the "type" field**

Modify the payload to include the `type` field:

```python
payload = f'{{"ietf-interfaces:interface": {{"name": "{TARGET_INTERFACE}", "description": "{DESCRIPTION}", "type": "iana-if-type:softwareLoopback", "enabled": {str(ENABLED).lower()}}}}}'
```

5. **Final Code Execution**

Now, execute your updated script again. It should update the interface's description without errors.

## Conclusion:

In Lab 10, we learned about the nuances of RESTCONF operations, especially the difference between POST and PUT, and the importance of providing all necessary details in our payload. By resolving encountered errors step-by-step, we gained a deeper understanding of how RESTCONF works and how to troubleshoot issues.