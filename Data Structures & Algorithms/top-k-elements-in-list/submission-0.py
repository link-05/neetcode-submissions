class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key = {}
        bucket = [[] for _ in range(len(nums))]
        i = 0
        # Make buckets of size N
        # Fill bucket 
        for num in nums:
            if num in key:
                bucket[key[num]].append(num)
            else:
                bucket[i].append(num)
                key[num] = i
                i += 1
        bucket.sort(key=len)
        ret = []
        for i in range(1, k + 1):
            ret.append(bucket[-i][0])
        return ret

