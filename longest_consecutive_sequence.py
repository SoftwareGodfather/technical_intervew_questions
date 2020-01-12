class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = dict()
        for elem in nums:
            visited[elem] = False
        maxLen = 0
        
        for elem in nums:
            curLen = 0
            if not visited[elem]:
                visited[elem] = True
                curLen += 1
                
                prevVal = elem - 1
                while prevVal in visited.keys():
                    visited[prevVal] = True
                    curLen += 1
                    prevVal -= 1
                    
                nextVal = elem + 1
                while nextVal in visited.keys():
                    visited[nextVal] = True
                    curLen += 1
                    nextVal += 1
                
                if curLen > maxLen:
                    maxLen = curLen
        
        return maxLen
