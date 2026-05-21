class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # Regular expression, replace all non a-z character class with empty
        s = re.sub(r'[^a-z0-9]', '', s)
        lPtr, rPtr = 0, len(s) - 1
        # Close in toward the center like binary search
        while lPtr < rPtr:
            if s[lPtr] != s[rPtr]:
                return False
            lPtr += 1
            rPtr -= 1
        return True