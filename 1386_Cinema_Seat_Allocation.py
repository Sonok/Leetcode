from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = defaultdict(int)
        for r,c in reservedSeats:
            if 2 <= c <= 9:
                res[r] |= 1 << (c-2)
        
        left_mask = 0b00001111
        middle_mask = 0b00111100
        right_mask = 0b11110000

        ret = (n - len(res)) * 2 # every row has two avaliable 

        for row, series in res.items():
            
            left_avail = (left_mask & series) == 0
            right_avail = (right_mask & series) == 0

            if(left_avail and right_avail):
                ret += 2
            elif(left_avail or right_avail or series & middle_mask == 0):
                ret += 1
        
            
        return ret
        