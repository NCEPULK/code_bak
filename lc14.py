from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = 200
        for key in strs:
            minLength = min(minLength,len(key))
        for length in range(1,minLength+1):
            base = strs[0][:length]
            for key in strs:
                if key[:length]!=base:
                    return key[:length-1]
        return strs[0][:minLength]

solution = Solution()
lis = ["flower","flow","flight"]
print(solution.longestCommonPrefix(lis))