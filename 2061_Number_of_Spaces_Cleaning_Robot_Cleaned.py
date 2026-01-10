# touch 2061_Number_of_Spaces_Cleaning_Robot_Cleaned.py
from collections import deque
class Solution:

    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        if room[0][0] == 1:
            return 0
        m, n = len(room), len(room[0])

        visited = set()

        queue = deque()
        queue.append((0,0, 'E'))

        clockwise = ['N', 'E', 'S', 'W'] # rotate around

        while queue:
            i, j, direction = queue.popleft()
            if (i,j, direction) in visited:
                 break
            visited.add((i,j, direction)) 
            # if we been here before we jump away 

            orgI, orgJ = i, j # incase we need to pivot

            if direction == 'E':
                j += 1
            elif direction == 'W':
                j -= 1
            elif direction == 'S':
                i += 1
            else:
                i -= 1
            
            print(i , j, direction)
            if 0 <= i < m and 0 <= j < n and room[i][j] == 0: # no need to pivot
                queue.append((i,j, direction))
            else: # we need to pivot
                newDir = (clockwise.index(direction) + 1) % 4
                queue.append((orgI, orgJ, clockwise[newDir]))
        
        print(visited)
        s = set()
        for i, j, dr in visited:
            s.add((i,j))
        return len(s)


