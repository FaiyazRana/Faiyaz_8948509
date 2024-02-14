def reverse_string(input_str):
    """
    Reverse a given string.

    Args:
    - input_str (str): The input string.

    Returns:
    - str: The reversed string.
    """
    return input_str[::-1]

def factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
    - n (int): The input number.

    Returns:
    - int: The factorial of the input number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)