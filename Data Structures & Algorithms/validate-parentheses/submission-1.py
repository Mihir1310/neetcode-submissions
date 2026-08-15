class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for char in s:
            if char in ["(", "{", "["]:
                temp.append(char)
            else:
                if temp and (char == ")" and temp[-1] == "(" or
                   char == "]" and temp[-1] == "[" or
                   char == "}" and temp[-1] == "{"):
                    temp.pop()
                else:
                    return False
        return True if len(temp) == 0 else False

        