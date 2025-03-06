# Lab: Clean Code Basics - Building a List Calculator in Python

## Introduction

In this lab, we will continue our journey into clean code and good practices in Python. We will build a List Calculator using functions and classes, which are fundamental building blocks in Python. Initially, we will define functions to perform various mathematical operations, and later, we will encapsulate them into a class. Throughout the lab, we will emphasize writing clean, well-documented, and efficient code.

### 1. Define Functions
Let's define three functions: one for squaring numbers, one for calculating square roots (marked with `TODO`), and one for division (marked with `FIXME` for handling division by zero).

```python
# Function to square each element in a list
def square_list(numbers):
    """
    This function squares each number in the list.
    :param numbers: List of numbers to be squared.
    :return: List of squared numbers.
    """
    return [each_num ** 2 for each_num in numbers]

# TODO: Implement the square root function
def square_root_list(numbers):
    """
    This function calculates the square root of each number in the list.
    :param numbers: List of numbers for which the square root is to be calculated.
    :return: List of square roots.
    """
    # Write your code here
    pass

# FIXME: Handle division by zero
def divide_list(numbers, divisor):
    """
    This function divides each number in the list by the divisor.
    :param numbers: List of dividends.
    :param divisor: The divisor.
    :return: List of results of the division.
    """
    return [each_num / divisor for each_num in numbers]
```

### 2. Define Calculator Class
Organize the functions we have defined into a class structure to create our List Calculator. Remember to keep the code clean, structured, and well-documented with docstrings and comments.

```python
class ListCalculator:
    def __init__(self):
        """
        Constructor for the ListCalculator class.
        Initializes without any parameters.
        """
        pass

    def square(self, numbers):
        """
        Squares each number in the list.
        :param numbers: List of numbers to be squared.
        :return: List of squared numbers.
        """
        return [each_num ** 2 for each_num in numbers]

    def square_root(self, numbers):
        """
        Calculates the square root of each number in the list.
        :param numbers: List of numbers for which the square root is to be calculated.
        :return: List of square roots.
        """
        # TODO: Implement the square root method
        pass

    def divide(self, numbers, divisor):
        """
        Divides each number in the list by the divisor.
        :param numbers: List of dividends.
        :param divisor: The divisor.
        :return: List of results of the division.
        """
        # FIXME: Handle division by zero
        return [each_num / divisor for each_num in numbers]
```

#### Usage

After modifying the class, create an instance of the ListCalculator and call the methods to perform the respective operations on the list, passing the list of numbers as an argument in the method calls.

```python
# Creating a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Creating an instance of ListCalculator
calculator = ListCalculator()

# Using the methods to perform operations and print the results
print("Squared List:", calculator.square(numbers_list))
print("Square Root List:", calculator.square_root(numbers_list))
print("Divided List by 2:", calculator.divide(numbers_list, 2))
```

### Conclusion
This lab allowed us to explore the implementation of a List Calculator in Python using functions and classes while adhering to clean coding practices. Addressing the `TODO` and `FIXME` tasks will help reinforce the principles of writing maintainable and scalable code. By organizing the code using classes, we have laid down a structured foundation for expanding our List Calculator with additional features and functionalities in the future.

### Extra - Type Hit

```python
from typing import List

def square(numbers: List[float]) -> List[float]:
    """
    Squares each number in the list.
    :param numbers: List of numbers to be squared.
    :return: List of squared numbers.
    """
    return [each_num ** 2 for each_num in numbers]
```

```python
from typing import List, Union

def divide(numbers: List[Union[int, float]], divisor: Union[int, float]) -> List[Union[int, float]]:
    """
    Divides each number in the list by the divisor.
    :param numbers: List of dividends.
    :param divisor: The divisor.
    :return: List of results of the division.
    """
    # FIXME: Handle division by zero
    return [each_num / divisor for each_num in numbers]
```