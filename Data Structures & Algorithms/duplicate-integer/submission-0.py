class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for n in nums:
            if dict.get(n) != None:
                return True
            else:
                dict[n] = 1
        return False