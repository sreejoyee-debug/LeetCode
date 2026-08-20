class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expsum = n * (n + 1) // 2
        totalsum = sum(nums)
        return expsum - totalsum  




        