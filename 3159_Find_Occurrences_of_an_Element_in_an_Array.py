class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        lst = [] 
        for i, val in enumerate(nums):
            if val == x:
                lst.append(i)
        for i in range(len(queries)):
            if len(lst) < queries[i]:
                queries[i] = -1
            else:
                queries[i] = lst[queries[i] - 1]
                #queries[i] = lst[queries[i] - 1]
        return queries
        