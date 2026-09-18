class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low=0
        high= len(nums)-1
        ans=nums[0]
        while(low <= high):
            mid=(low+high)//2
            if (nums[low] <= nums[high]):
                if nums[low] == target:
                    return low
                if nums[high] == target:
                    return high
                if nums[mid] == target:
                    return mid
            if (nums[low] <= nums[mid]):
                if nums[low] == target:
                    return low
                    break
                low=mid+1
            else:
                if nums[low] == target:
                    return low
                    break
                high=mid - 1
        return -1

       
        