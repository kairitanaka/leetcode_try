class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = []
        
        for i ,c in enumerate(strs[0]):
            for word in strs[1:]:
                if i>=len(word) or word[i] != c:
                    return strs[0][:i]
        return strs[0]
                

            
