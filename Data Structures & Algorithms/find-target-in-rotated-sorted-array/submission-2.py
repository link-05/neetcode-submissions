class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        cut = -1
        # find the cut
        while low < high:
            if nums[low] < nums[high]:
                break
            mid = (low+high)//2
            if nums[mid] < nums[low]:
                high = mid
            else:
                low = mid + 1
        cut = low
        # check where to 
        if target == nums[cut]:
            return cut
        elif target < nums[cut]:
            return -1
        
        if target >= nums[0] and cut != 0:
            low = 0
            high = cut - 1
        else:
            low = cut
            high = len(nums) - 1
            
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

            