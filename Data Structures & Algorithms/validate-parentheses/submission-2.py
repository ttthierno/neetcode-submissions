class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        closetoOpen = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in closetoOpen:
                if ans and ans[-1] == closetoOpen[i]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(i)
        return True if not ans else False