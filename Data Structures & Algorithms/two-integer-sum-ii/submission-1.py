class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr = 0 
        ptr2 = 1
        while ptr < len(numbers):
            ptr2 = ptr + 1
            while ptr2 < len(numbers):
                if numbers[ptr] + numbers[ptr2] == target:
                    return [ptr + 1, ptr2 + 1]
                elif numbers[ptr] + numbers[ptr2] > target:
                    break
                else:
                    ptr2+=1 
            ptr += 1
        
                         