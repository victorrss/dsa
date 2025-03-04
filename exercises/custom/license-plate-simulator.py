# Problem: License Plate Simulator

# Description:
# You are tasked with building a system that computes a car's license plate number from an integer input. 
# The system should convert the input number to a license plate string according to the following rules:

# Numeric Plates:

# For input numbers from 0 to 99,999, the plate is the 5-digit representation of the number, zero-padded on the left.
# Example:
# Input: 0 → Output: 00000
# Input: 1 → Output: 00001
# Input: 99999 → Output: 99999
# Single-Letter Plates:

# For input numbers from 100,000 to 359,999, the plate is formatted as a letter (from A to Z) followed by a 4-digit number (zero-padded on the left).
# The range for each letter covers 10,000 numbers.
# Example:
# Input: 100000 → Output: A0000
# Input: 110000 → Output: B0000
# Double-Letter Plates:

# For input numbers starting from 360,000, the plate is formatted as two letters (starting with AA) followed by a 3-digit number (zero-padded on the left).
# Example:
# Input: 360000 → Output: AA000
# Input: 360999 → Output: AA999
# Input: 361000 → Output: AB000
# Input Format:

# A single integer representing the car’s plate number code.
# Output Format:

# A string representing the corresponding license plate.

def number_to_plate(num: int) -> str:
    # TODO: Implement the function to convert the number to a license plate string
    pass

def run_tests():
    tests = [
        (0, "00000"),
        (1, "00001"),
        (99999, "99999"),
        (100000, "A0000"),
        (110000, "B0000"),
        (360000, "AA000"),
        (360999, "AA999"),
        (361000, "AB000"),
    ]
    
    for idx, (inp, expected) in enumerate(tests, start=1):
        result = number_to_plate(inp)
        print(f"Test {idx}: {'Pass' if result == expected else f'Fail (Expected: {expected}, Got: {result})'}")

if __name__ == '__main__':
    run_tests()
