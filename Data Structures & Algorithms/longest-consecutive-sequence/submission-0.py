class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        longest = 0
        for num in sets:
            # Check each starting sequence 
            if num - 1 not in sets:
                tempLong = 1
                while num + tempLong in sets:
                    tempLong+=1
                if tempLong > longest:
                    longest = tempLong
        return longest
                
