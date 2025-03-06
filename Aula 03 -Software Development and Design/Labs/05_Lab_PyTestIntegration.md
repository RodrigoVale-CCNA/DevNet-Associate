# Lab: PyTest and Good Practices

### Objective

Extend the previous lab to perform integration testing using PyTest. In this lab, we will introduce another method in the `ListCalculator` module and test the integration of both methods.

### Prerequisites: Completion of the previous unit testing lab.

### 1. Create a Sequence Generator Module
Create a new Python module, `sequence_generator_module.py`, with a class `SequenceGenerator` that has a method to generate a sequence of integers.

```python
class SequenceGenerator:
    """
    A class containing a method to generate a sequence of integers.
    """

    @staticmethod
    def generate_sequence(n):
        """
        Generates a sequence of integers from 1 to n.
        """
        return list(range(1, n + 1))
```

### 2. Create Integration Test
Create a new test file, `test_integration.py`. Import both the `ListCalculator` and `SequenceGenerator` modules and write a test to check the integration of `generate_sequence` and `square` methods.

```python
import pytest
from sequence_generator_module import SequenceGenerator
from list_calculator_module import ListCalculator

def test_integration():
    """
    Test the integration of the generate_sequence method from SequenceGenerator 
    and square method from ListCalculator.
    """
    n = 3
    
    # Generate a sequence
    sequence = SequenceGenerator.generate_sequence(n)
    
    # Check if the output type of generate_sequence matches the input type of square
    assert isinstance(sequence, list), "The output of generate_sequence should be a list"
    assert all(isinstance(num, int) for num in sequence), "All elements in the sequence should be integers"
    
    # Calculate the square of the sequence and check if the output is as expected
    squared_list = ListCalculator.square(sequence)
    assert squared_list == [1, 4, 9], "The squared list is not as expected"
```

### 3. Run Integration Test
Navigate to the project directory in your terminal and run the integration test using the following command:

```bash
pytest test_integration.py
```

Observe the output. If the integration test passes, PyTest will display a message indicating successful execution. If it fails, PyTest will provide detailed information on the discrepancy.

## Conclusion
This lab demonstrated how to perform integration testing to ensure that individual units or methods in a module work together correctly. Regular integration testing is crucial as it helps identify issues early in the development cycle, ensuring the reliability of the software.