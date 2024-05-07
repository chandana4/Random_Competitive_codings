class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0:
            return True
        for let in t:
            if i < len(s) and s[i] == let:
                i += 1
        if i == len(s):
            return True
        else:
            return False
