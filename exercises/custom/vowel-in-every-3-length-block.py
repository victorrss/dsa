"""
// Title: Vowel in Every 3-Length Block
// Task: Given a string s, split it into consecutive, non-overlapping blocks of length 3 (ignore the last block if it has fewer than 3 chars). For each full block, return True if it contains at least one vowel (a,e,i,o,u, case-insensitive), otherwise False.

// Example
// s = "CodeSignal" → blocks: "Cod", "eSi", "gna" → result: [True, True, False].

// Constraints
// 1 <= len(s) <= 10^5 — O(n) solution expected.

// Python solution + tests
"""
from typing import List

def vowel_blocks(s: str) -> List[bool]:
    vowels = "aeiouAEIOU"
    result = []
    for i in range(0, len(s) // 3 * 3, 3):   # só blocos completos
        block = s[i:i+3]
        result.append(any(c in vowels for c in block))
    return result

# quick tests
if __name__ == "__main__":
    assert vowel_blocks("CodeSignal") == [True, True, False]          # "Cod","eSi","gna"
    assert vowel_blocks("abcdef") == [True, True]                      # "abc","def"
    assert vowel_blocks("xyz") == [False]                              # "xyz"
    assert vowel_blocks("aeioubcdef") == [True, False, True]           # "aei","oub","cde" -> last "f" ignored
    assert vowel_blocks("a") == []                                     # no full block
    print("All tests passed!")
