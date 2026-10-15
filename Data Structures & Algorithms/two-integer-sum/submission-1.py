class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            for j in range(len(nums)-i-1):
                nidx = i+1+j
                num2 = nums[nidx]
                if(num + num2 == target):
                    return [i, nidx]
