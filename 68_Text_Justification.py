class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        pos = 0 # position we start the word look right to be greedy?
        out = []

        while pos < len(words):
            run = 0 # running length
            i = 0 # how many words have u taken so far? 
            # i - 1 should count space
            line = []
            while pos + i < len(words):
                if(run + i <= maxWidth - len(words[pos + i])):
                    run += len(words[pos + i])
                    line.append(words[pos + i])
                    i += 1
                else:
                    break
            if pos + i != len(words):
                out.append(self.formatString(line, run, maxWidth))
            else:
                out.append(' '.join(line) + ' ' * (maxWidth - run - len(line) + 1))
            pos += i
        return out
    
    def formatString(self, line: str, run: int, width: int) -> str:
        if(len(line) == 1):
            return line[0] + " " * (width - run)
        
        leftOver = (width - run) % (len(line) - 1)
        space = (width - run) // (len(line) - 1)

        ret = ""
        for i in range(leftOver):
            ret += line[i]
            ret += " " * (space + 1)
        
        for i in range(leftOver, len(line) - 1):
            ret += line[i]
            ret += " " * (space)
        ret += line[-1]

        return ret
            


             
            
                    
            class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        pos = 0 # position we start the word look right to be greedy?
        out = []

        while pos < len(words):
            run = 0 # running length
            i = 0 # how many words have u taken so far? 
            # i - 1 should count space
            line = []
            while pos + i < len(words):
                if(run + i <= maxWidth - len(words[pos + i])):
                    run += len(words[pos + i])
                    line.append(words[pos + i])
                    i += 1
                else:
                    break
            if pos + i != len(words):
                out.append(self.formatString(line, run, maxWidth))
            else:
                out.append(' '.join(line) + ' ' * (maxWidth - run - len(line) + 1))
            pos += i
        return out
    
    def formatString(self, line: str, run: int, width: int) -> str:
        if(len(line) == 1):
            return line[0] + " " * (width - run)
        
        leftOver = (width - run) % (len(line) - 1)
        space = (width - run) // (len(line) - 1)

        ret = ""
        for i in range(leftOver):
            ret += line[i]
            ret += " " * (space + 1)
        
        for i in range(leftOver, len(line) - 1):
            ret += line[i]
            ret += " " * (space)
        ret += line[-1]

        return ret
            
