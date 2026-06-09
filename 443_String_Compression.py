class Solution:
    def compress(self, chars: List[str]) -> int:
        # we should have a write index where we are writing to our values 
        # we should have. read index. We see of length n and then we lengthen it
        n = len(chars)
        read = write = 0
        while(read < n): # since write <= read
            groupSize = 1
            while(read + groupSize < n and chars[read + groupSize] == chars[read]):
                groupSize += 1

            chars[write] = chars[read]
            write += 1 

            if groupSize > 1:
                for char in str(groupSize): 
                    chars[write] = char
                    write += 1
                    
            read += groupSize 

        return write
            
