class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = [1] * len(nums)
        post = [1] * len(nums)
        acc = 1
        for x in range(0, len(nums)):
            acc *= nums[x]
            pre[x] = acc        
        acc = 1
        for y in range(1, len(nums) + 1):
            acc *= nums[-y]
            post[-y] = acc
        for i in range(0, len(res)):
            if i == 0 or i == len(res) - 1:
                if i == 0:
                    res[i] = post[i+1]
                if i == len(res) - 1:
                    res[i] = pre[i-1]
            else:
                res[i] = pre[i-1] * post[i+1]
        return res

