class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = sorted(enumerate(nums), key=lambda x: x[1])
        left=0
        right=len(nums)-1
        while left < right:
            if arr[left][1] + arr[right][1] == target:
                return [arr[left][0], arr[right][0]]
            elif arr[left][1] + arr[right][1] < target:
                left+=1
            else:
                right-=1

        

        