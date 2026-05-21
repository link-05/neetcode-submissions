class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        # From 0 to n - 1
        for i in range(len(nums)):
            # The diff from target right now
            diff = target - nums[i]
            # If diff from target exists in dict then return else add to dict
            if diff in dict:
                return [(dict[diff]), i]
            else:
                dict[nums[i]] = i
        # No edge case for false return because an answer guarantee to exist