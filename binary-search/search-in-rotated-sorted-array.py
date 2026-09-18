class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low=0
        high= len(nums)-1
        ans=nums[0]
        while(low <= high):
            mid=(low+high)//2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                # left half [low..mid] is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # right half [mid..high] is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

       
        