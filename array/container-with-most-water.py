class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater=0
        left=0
        n = len(height)
        right=n-1
        while left<right:
            w=right-left
            h=min(height[left],height[right])
            ans= w*h
            maxwater=max(maxwater,ans)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxwater
        

        