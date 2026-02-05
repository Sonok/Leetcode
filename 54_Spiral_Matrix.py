from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        dirs = [(0, 1), (1,0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        curr = (0,0)
        direction = 0
        path = []

        path.append(matrix[0][0])
        visited.add((0,0))

        while(len(visited) < m * n):
            x, y = curr[0], curr[1]
            dx, dy = dirs[direction] # change of direction
            
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                curr = (nx, ny)
                visited.add((nx, ny))
                path.append(matrix[nx][ny])
            else:
                direction = (direction + 1) % 4

        return path

    