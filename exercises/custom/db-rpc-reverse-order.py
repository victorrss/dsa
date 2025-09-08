"""
This is a test case for a mock RPC-based database that supports two operations:
- Insert(key): inserts a key in lexicographical order
- Get(prefix): returns all keys greater than or equal to prefix in lexicographical order

The challenge is to implement OurInsert and OurGet, where:
- OurInsert inserts a key using the Insert() from database RPC
- OurGet retrieves keys in reverse lexicographical order (descending) and using the Get() from database RPC
"""

# ---------------------------
# Mock database - DO NOT CHANGE THIS PART
# ---------------------------
db = []

def Insert(key: str):
    """Insert key into the database in lexicographical order."""
    db.append(key)
    db.sort()

def Get(prefix: str):
    """Return all keys >= prefix in lexicographical ascending order."""
    return [k for k in db if k >= prefix]

# ---------------------------
# Transformation functions
# ---------------------------
def transform(s: str) -> str:
    """
    Transform a string to invert its lexicographical order.
    Only works for lowercase a-z.
    """
    return "".join(chr(ord('z') - (ord(c) - ord('a'))) for c in s)

# ---------------------------
# OurInsert and OurGet -  ASCII transformation → elegant, works well in interviews, quick to implement.
# ---------------------------
def OurInsert(key: str):
    """Insert a key using transformed lexicographical order."""
    Insert(transform(key))

def OurGet(prefix: str):
    """
    Retrieve all keys >= prefix in reverse lexicographical order.
    """
    transformed_prefix = transform(prefix)
    result = Get(transformed_prefix)
    original = [transform(x) for x in result]
    return sorted(original, reverse=True)

# # ---------------------------
# # OurInsert and OurGet - ALTERNATIVE VERSION
# # ---------------------------
# def OurInsert(key: str):
#     Insert(key)

# def OurGet(prefix: str):
#     """
#     Return keys in reverse lexicographical order starting from prefix.
#     Only returns keys <= the largest key < prefix if prefix is beyond last element.
#     """
#     all_keys = Get("")  # get all keys
#     # Filter keys that are <= prefix if prefix is less than max key
#     if prefix:
#         # keys <= largest key smaller than prefix
#         filtered = [k for k in all_keys if k <= prefix]  
#     else:
#         filtered = all_keys
#     return list(reversed(filtered))


# ---------------------------
# Test cases
# ---------------------------
def test_rpc_reverse_order():
    # Reset database
    global db
    db = []

    # Insert keys
    OurInsert("a")
    OurInsert("b")
    OurInsert("c")
    OurInsert("d")
    OurInsert("f")

    # Test OurGet
    assert OurGet("b") == ["b","a"], f"Expected ['b','a'], got {OurGet('b')}"
    assert OurGet("e") == ["d","c","b","a"], f"Expected ['d','c','b','a'], got {OurGet('e')}"
    assert OurGet("a") == ['a'], f"Expected ['a'], got {OurGet('a')}"
    assert OurGet("")  == ["f","d","c","b","a"], f"Expected ['f','d','c','b','a'], got {OurGet('')}"

    print("All test cases passed!")

# ---------------------------
# Run tests
# ---------------------------
if __name__ == "__main__":
    test_rpc_reverse_order()
