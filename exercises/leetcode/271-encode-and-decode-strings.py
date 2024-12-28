class Codec:
    def __init__(self):
        self.scape = "&v"

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""
        for s in strs:
            encoded += s.replace("&", "&&") + self.scape
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ans = []
        i = 0
        curr_line = ""
        while i < len(s):
            if s[i : i + 2] == self.scape:
                ans.append(curr_line)
                curr_line = ""
                i += 2
            elif s[i : i + 2] == "&&":
                curr_line += "&"
                i += 2
            else:
                curr_line += s[i]
                i += 1
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
