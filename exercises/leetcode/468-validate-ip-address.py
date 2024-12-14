class Solution:
    def tryParseInt(self, strInt):
        try:
            return int(strInt)
        except Exception:
            return None

    def tryParseHex(self, strHex):
        try:
            return int(strHex, 16)
        except Exception:
            return None

    def isIPv4(self, queryIP):
        octets = queryIP.split(".")
        # Validing octets
        if len(octets) != 4:
            return False

        for octet in octets:
            # Validing length
            if len(octet) < 1 or len(octet) > 3:
                return False
            # Validing leading zeros
            if len(octet) > 1 and octet[0] == "0":
                return False
            # Validing range and invalid caracters
            octetInt = self.tryParseInt(octet)
            if octetInt == None or (octetInt < 0 or octetInt > 255):
                return False

        return True

    def isIPv6(self, queryIP):
        parts = queryIP.split(":")
        # Validing parts
        if len(parts) != 8:
            return False

        for part in parts:
            # Validing length
            if len(part) < 1 or len(part) > 4:
                return False
            # Validing range and invalid caracters
            partHex = self.tryParseHex(part)
            max16bits = 2**16 - 1
            if partHex == None or (partHex < 0 or partHex > max16bits):
                return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if self.isIPv4(queryIP):
            return "IPv4"
        elif self.isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
