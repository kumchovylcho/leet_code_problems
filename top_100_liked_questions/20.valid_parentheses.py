# https://leetcode.com/problems/valid-parentheses/description/

class Solution:

    def isValid(self, s: str) -> bool:
        parentheses = list(s)

        valid_parentheses = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        matches = []

        while parentheses:
            current = parentheses.pop(0)

            if current in valid_parentheses.keys():
                matches.append(current)
                continue

            for open_p, close_p in valid_parentheses.items():
                if current == close_p and matches and matches[-1] == open_p:
                    matches.pop()
                    break

            else:
                return False

        if matches:
            return False

        return True