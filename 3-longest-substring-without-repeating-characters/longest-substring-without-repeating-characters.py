class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}      # char -> last seen index
        left = 0
        maxi = 0

        for right in range(len(s)):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1)

            maxi = max(maxi, right - left + 1)
            my_dict[s[right]] = right

        return maxi
        