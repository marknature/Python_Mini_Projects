'''
This script:
- Demonstrates key functions from the math module.
- Uses the random module to generate numbers and samples.
- Retrieves system information using the platform module.
- Uses aliasing to rename imported modules.
'''

import math as m
import random as rnd
import platform as pf

def math_demo():
    print("Math Module Demonstration")
    angle_deg = 45
    angle_rad = m.radians(angle_deg)
    print(f"Sin({angle_deg}°): {m.sin(angle_rad)}")
    print(f"Cos({angle_deg}°): {m.cos(angle_rad)}")
    print(f"Tan({angle_deg}°): {m.tan(angle_rad)}")
    print(f"Pi Constant: {m.pi}")
    print(f"Euler's Number: {m.e}")
    print("-" * 40)

def random_demo():
    print("Random Module Demonstration")
    rnd.seed(42)
    print("Random numbers:", [rnd.random() for _ in range(5)])
    print("Random integer (1-10):", rnd.randint(1, 10))
    sample_list = list(range(1, 11))
    print("Random Sample of 3:", rnd.sample(sample_list, 3))
    print("Random Choice:", rnd.choice(sample_list))
    print("-" * 40)

def platform_demo():
    print("Platform Module Demonstration")
    print("System:", pf.system())
    print("Version:", pf.version())
    print("Machine:", pf.machine())
    print("Processor:", pf.processor())
    print("Python Implementation:", pf.python_implementation())
    print("Python Version Tuple:", pf.python_version_tuple())
    print("-" * 40)

def main():
    math_demo()
    random_demo()
    platform_demo()

if __name__ == "__main__":
    main()

