# https://leetcode.com/problems/valid-anagram/?envType=daily-question&envId=2023-12-16


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        other_word_result = ""
        for i in range(len(s)):
            current_letter = s[i]

            if current_letter not in t:
                return False

            t = t.replace(current_letter, "", 1)
            other_word_result += current_letter


        return s == other_word_result and not t




real = "a"
unreal = "ab"
solution = Solution()
result = solution.isAnagram(real, unreal)
print(result)