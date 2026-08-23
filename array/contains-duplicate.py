'''BETTER SOLUTION 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr= sorted(nums)
        for i in range (len(arr)-1):
            if arr[i]==arr[i+1]:
                return True
        return False
'''

'''OPTIMAL SOLUTION-HASHMAP'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 1:
                return True
        return False
        

        