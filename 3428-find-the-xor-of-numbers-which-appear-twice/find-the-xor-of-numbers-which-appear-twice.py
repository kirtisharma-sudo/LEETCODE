class Solution(object):
    def duplicateNumbersXOR(self, nums):
        seen = set()
        ans = 0
        for i in nums:
            if i in seen:
                ans ^= i
            else:
                seen.add(i)
        return ans