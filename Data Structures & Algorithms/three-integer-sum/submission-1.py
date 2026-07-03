class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            # Ignore already tested value
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Do a 
            low = i + 1
            high = len(nums) - 1
            # Perform 2 integer sum II with remove duplicate
            while low < high: 
                total = nums[low] + nums[high] + nums[i]
                if total == 0:
                    res.append([nums[low], nums[high], nums[i]])
                    low+=1
                    high-=1
                    while low < high and nums[low] == nums[low-1]:
                        low+=1
                elif total > 0:
                    high -= 1
                else:
                    low += 1
        return res
