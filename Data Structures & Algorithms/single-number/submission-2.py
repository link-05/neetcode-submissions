class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # Bitwise manipulation, xor all elements, 
            # the other elements cancel each other the second time going through.
            res = res^num
        return res