class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        count = 0
        n = len(nums)
        dic = {} # should make a dic for number of times num[i] - rev(num[i])
        for val in nums:
            valRev = (int)((str(val)[::-1]))
            diff = val - valRev
            if diff in dic:
                count += dic[diff] # we add the number of occuernces
            # count += dic.get(diff, 0)
            dic[diff] = dic.get(diff, 0) + 1 # increment

        return count % MOD
        