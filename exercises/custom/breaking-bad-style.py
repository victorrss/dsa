# Problem: Breaking Bad Style

# Description:
# You are given a name (a string) and a list of element symbols (strings). 
# Your task is to write a function breaking_bad(name: str, symbols: List[str]) -> str that formats the name according to the following rules:

# For each word in the name, check if the beginning of the word (case-insensitive) matches any of the provided element symbols (also case-insensitive).
# If a match is found, wrap the matching prefix in square brackets.
# If no match is found for a word, leave it unchanged.
# Input Format:

# A string representing the name (which may contain multiple words separated by spaces).
# A list of strings representing the available element symbols.
# Output Format:

# A single string where each word is formatted following the rules above.
# Examples:

# Example 1:

# Input:
# name = "henry alba"
# symbols = ["H", "He", "Li", "Be", "B", "C", "N", "F", "Ne", "Na", "Co", "Ni", "Cu", "Ga", "Al", "Si", "Fa"]
# Explanation:
# The word "henry" has a prefix "He" (from the symbols) → becomes "[He]nry".
# The word "alba" has a prefix "Al" (from the symbols) → becomes "[Al]ba".
# Output:
# "[He]nry [Al]ba"
# Example 2:

# Input:
# name = "connor riddle"
# symbols = ["H", "He", "Li", "Be", "B", "C", "N", "F", "Ne", "Na", "Co", "Ni", "Cu", "Ga", "Al", "Si", "Fa"]
# Explanation:
# The word "connor" has a prefix "Co" → becomes "[Co]nnor".
# The word "riddle" does not match any symbol → remains unchanged.
# Output:
# "[Co]nnor riddle"
# Example 3:

# Input:
# name = "nicole carry"
# symbols = ["H", "He", "Li", "Be", "B", "C", "N", "F", "Ne", "Na", "Co", "Ni", "Cu", "Ga", "Al", "Si", "Fa"]
# Explanation:
# "nicole" starts with "Ni" → becomes "[Ni]cole".
# "carry" starts with "C" → becomes "[C]arry".
# Output:
# "[Ni]cole [C]arry"
# Example 4:

# Input:
# name = "jerry seinfeld"
# symbols = ["H", "He", "Li", "Be", "B", "C", "N", "F", "Ne", "Na", "Co", "Ni", "Cu", "Ga", "Al", "Si", "Fa"]
# Explanation:
# Neither "jerry" nor "seinfeld" have a matching prefix → remain unchanged.
# Output:
# "jerry seinfeld"
# Example 5:

# Input:
# name = "ben f gabe"
# symbols = ["H", "He", "Li", "Be", "B", "C", "N", "F", "Ne", "Na", "Co", "Ni", "Cu", "Ga", "Al", "Si", "Fa"]
# Explanation:
# "ben" starts with "Be" → becomes "[Be]n".
# "f" matches "F" → becomes "[F]".
# "gabe" starts with "Ga" → becomes "[Ga]be".
# Output:
# "[Be]n [F] [Ga]be"

def breaking_bad(name: str, symbols: list) -> str:
    # TODO: Implement the function to format the name in "Breaking Bad Style"
    # For each word in the name, check for a matching symbol (case-insensitive)
    # and wrap the matching prefix in square brackets.
    pass

def run_tests():
    symbols = ["H", "He", "Li", "Be", "B", "C", "N", "F", "Ne", "Na", "Co", "Ni", "Cu", "Ga", "Al", "Si", "Fa"]
    
    # Test case 1
    name = "henry alba"
    expected = "[He]nry [Al]ba"
    result = breaking_bad(name, symbols)
    print("Test 1:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")
    
    # Test case 2
    name = "connor riddle"
    expected = "[Co]nnor riddle"
    result = breaking_bad(name, symbols)
    print("Test 2:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")
    
    # Test case 3
    name = "nicole carry"
    expected = "[Ni]cole [C]arry"
    result = breaking_bad(name, symbols)
    print("Test 3:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")
    
    # Test case 4
    name = "jerry seinfeld"
    expected = "jerry seinfeld"
    result = breaking_bad(name, symbols)
    print("Test 4:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")
    
    # Test case 5
    name = "ben f gabe"
    expected = "[Be]n [F] [Ga]be"
    result = breaking_bad(name, symbols)
    print("Test 5:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    run_tests()
