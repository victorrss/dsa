class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 1 - Get the max word qty that I can get less than  maxWidth (adding one space)
        # 2 - calc the spaces between words (n-1)
        # 3 - last line should have only one space between words, all trailings in the right

        def howManyWordsUse(it):
            start = it
            length = 0
            while it < len(words) and length + len(words[it]) <= maxWidth:
                length += len(words[it]) + 1
                it += 1
            qty = it - start
            return [qty, length - qty]

        def buildLastLine(it, qty):
            s = ""
            while it < len(words) and qty > 0:
                s += words[it]
                if qty != 1:
                    s += " "
                it += 1
                qty -= 1

            trails = maxWidth - len(s)
            if trails > 0:
                s += " " * trails

            return s

        def buildLine(it, qty, spacesLength, extraSpaces):
            s = ""
            # if only one word
            if qty == 1:
                s += words[it]
                s += " " * spacesLength
                return s
            
            while it < len(words) and qty > 0:
                s += words[it]
                if qty != 1: # putting space only when is not the last
                    s += " " * spacesLength
                    if extraSpaces > 0:
                        s += " "
                        extraSpaces -= 1
                it += 1
                qty -= 1

            return s

        it = 0
        ans = []
        while it < len(words):
            qty, length = howManyWordsUse(it)
            spacesToJustify = maxWidth - length
            spacesPlaces = qty - 1
            spaceMinLength = spacesToJustify // spacesPlaces if spacesPlaces > 0 else spacesToJustify
            extraSpaces = spacesToJustify % spacesPlaces if spacesPlaces > 0 else 0

            isLastLine = it + qty >= len(words)
            if not isLastLine:
                ans.append(buildLine(it, qty, spaceMinLength, extraSpaces))
            else:
                ans.append(buildLastLine(it, qty))

            it += qty
        return ans
