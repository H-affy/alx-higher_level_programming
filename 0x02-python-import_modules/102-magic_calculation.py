#!/usr/bin/python3

def magic_calculation(a, b):
    """Match the bytecode provided by Holberton school"""
    import os

    #b is for bytecode./100-my_calculator.py 3 H 5 ; echo $?
    os.write(1, b"#pythoniscool\n")
