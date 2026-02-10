class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        for j in range(n):
            start = matrix[m-1][j] # start the bottom diagnol
             # we start off with index 0 
            steps = 1 # no need to check 0 step
            while j - steps >= 0 and m-1-steps >= 0:
                if matrix[m - 1 - steps][j - steps] != start:
                    return False
                steps += 1

        for i in range(m-1):
            start = matrix[i][n-1] # start the bottom diagnol
             # we start off with index 0 
            steps = 1 # no need to check 0 step
            while i - steps >= 0 and n-1-steps >= 0:
                if matrix[i - steps][n - 1 - steps] != start:
                    return False
                steps += 1

        return True
