class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            for j in words[i]:
                if(j == x):
                    ans.append(i)
                    break
        return ans
