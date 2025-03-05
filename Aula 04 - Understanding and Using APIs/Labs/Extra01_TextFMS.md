# Understanding and Using TextFSM with Python

TextFSM is a powerful Python library that enables the structured collection of data from text outputs, such as those from command-line interfaces (CLI) of network devices. It uses templates to structure data and make it easily manageable in Python scripts.

## How TextFSM Works

TextFSM employs templates that detail the desired structure and capture method for the data. These templates define specific values that the program should capture and how they are formatted in the output. TextFSM then uses these templates to parse the CLI outputs.

## Creating a TextFSM Template

For our example, let's use the CLI output of the command `show ip int brief`:

```plaintext
Interface              IP-Address      Status     Protocol
FastEthernet0/0        10.0.0.1        up         up      
FastEthernet0/1        unassigned      down       down
```

To structure this data using TextFSM, we will design the following template:

```plaintext
Value INTERFACE (\S+)
Value IP_ADDRESS (\S+)
Value STATUS (\S+)
Value PROTOCOL (\S+)

Start
  ^Interface\s+IP-Address\s+Status\s+Protocol
  ^${INTERFACE}\s+${IP_ADDRESS}\s+${STATUS}\s+${PROTOCOL} -> Record
```

## Breaking Down the Template

- The `Value` keyword defines the variables we want to capture. The value name is followed by a regular expression detailing its format.
  
- The `Start` state is where the parsing begins. In our template, the first line under `Start` matches the header of the CLI output. 
  
- The next line captures the values we want based on the `Value` definitions.

## Using TextFSM with Python

To utilize TextFSM in Python:

1. Install TextFSM with `pip install textfsm`.
2. Create a TextFSM template file (e.g., `template.txt`).
3. Use Python to parse CLI outputs with the template.

```python
import textfsm

# Carregar o template
with open("template.txt", 'r') as template_file:
    template = textfsm.TextFSM(template_file)

# Sample command output
command_output = """
Interface              IP-Address      Status     Protocol
FastEthernet0/0        10.0.0.1        up         up      
FastEthernet0/1        unassigned      down       down
"""
parsed_results = template.ParseText(command_output)

# Imprimir resultados analisados
for result in parsed_results:
    print(result)
```

The script will structure the `command_output` according to the given template, producing a structured and easy-to-manage output.