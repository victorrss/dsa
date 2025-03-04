# **Problem: Decoding a Compressed String**

# **Description:**  
# You are given a compressed string that follows a specific encoding pattern. 
# In this pattern, a substring is enclosed in parentheses and is immediately followed by a multiplier enclosed in curly braces. 
# This multiplier indicates how many times the substring should be repeated. 
# The compression can be nested, meaning that a compressed substring may contain other compressed segments.

# **Input Format:**  
# - A single line containing the compressed string.
# - The string can include:
#   - Alphabetical characters (a–z, A–Z);
#   - Parentheses `(` and `)` that delimit the substrings;
#   - Curly braces `{` and `}` that contain a positive integer multiplier.

# **Output Format:**  
# - A single line containing the decoded (expanded) string.

# **Rules and Considerations:**  
# - Every occurrence of the pattern `(substring){n}` should be expanded into the substring repeated `n` times.
# - The compression can be nested. For example, in `((abc){2}){3}`, the inner compressed string should be decoded first, then the outer one.
# - The input is guaranteed to be well-formatted (all parentheses and curly braces are properly closed, and the multipliers are valid integers).

# **Examples:**

# 1. **Example 1:**  
#    - **Input:**  
#      `(aa){2}(b){3}`  
#    - **Explanation:**  
#      - `(aa){2}` expands to `"aa" * 2 = "aaaa"`.  
#      - `(b){3}` expands to `"b" * 3 = "bbb"`.  
#      - Final result: `"aaaa" + "bbb" = "aaaaabbb"`.  
#    - **Output:**  
#      `aaaaabbb`

# 2. **Example 2:**  
#    - **Input:**  
#      `((aaa){3}){3}`  
#    - **Explanation:**  
#      - First, decode the inner segment: `(aaa){3}` expands to `"aaa" repeated 3 times = "aaaaaaaaa"` (9 "a" characters).  
#      - Then, the outer pattern repeats that result 3 times, resulting in a total of 27 "a" characters.  
#    - **Output:**  
#      `aaaaaaaaaaaaaaaaaaaaaaaaaaa` *(27 "a"s)*

# 3. **Example 3:**  
#    - **Input:**  
#      `(ab(c){2}){3}`  
#    - **Explanation:**  
#      - The inner pattern `(c){2}` expands to `"cc"`.  
#      - This results in the substring `"abcc"`.  
#      - Repeating `"abcc"` 3 times gives `"abccabccabcc"`.  
#    - **Output:**  
#      `abccabccabcc`

def decode_string(s: str) -> str:
    # TODO: Implement the function to decode the compressed string
    pass

def run_tests():
    # Test case 1:
    input_str = "(aa){2}(b){3}"
    expected = "aaaaabbb"
    result = decode_string(input_str)
    print("Test 1:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")

    # Test case 2:
    input_str = "((aaa){3}){3}"
    expected = "a" * 27  # 27 "a" characters
    result = decode_string(input_str)
    print("Test 2:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")

    # Test case 3:
    input_str = "(ab(c){2}){3}"
    expected = "abccabccabcc"
    result = decode_string(input_str)
    print("Test 3:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    run_tests()
