class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = Counter(t)
        total = 0
        required = len(count_t)
        l, r = 0, 0
        window = {}
        ans_l, ans_r, ans_len = -1, -1, float("inf")

        while r < len(s):
            cur_r = s[r]
            if cur_r in count_t:
                window[cur_r] = window.get(cur_r, 0) + 1
                if window[cur_r] == count_t[cur_r]:
                    total += 1

            while l < len(s) and total == required:
                # check and record the answer
                cur_len = r - l + 1
                if cur_len < ans_len:
                    ans_l, ans_r, ans_len = l, r, cur_len

                cur_l = s[l]
                if cur_l in count_t:
                    window[cur_l] = window.get(cur_l, 0) - 1
                    if window[cur_l] < count_t[cur_l]:
                        total -= 1
                l += 1
            r += 1

        if ans_l != -1:  # if we found a min window substring
            return s[ans_l : ans_r + 1]
        else:
            return ""
