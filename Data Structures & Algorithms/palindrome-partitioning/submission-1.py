class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        # Palindrome two pointer
        def isPalindrome(w, l, r):
            while l < r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True
        # Every possible permutation
        def dfs(j, i):
            # If i goes out of range 
            if i >= len(s):
                # add the parts that are palindrome if at a i == j
                if i == j:
                    res.append(part.copy())
                return
            # if s between j to i range is palindrome
            if isPalindrome(s, j, i):
                # Add that palindrome to part
                part.append(s[j:i+1])
                # dfs to check 1 further
                dfs(i+1, i+1)
                part.pop()
            # j to next i check
            dfs(j, i+1)
        dfs(0, 0)
        return res
        
