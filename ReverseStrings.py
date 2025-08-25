"""Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces."""

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = n - 1
        result = []

        while i >= 0:
         
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0: break

          
            j = i
            while j >= 0 and s[j] != ' ':
                j -= 1

       
            result.append(s[j+1:i+1])

            i = j - 1  

        return " ".join(result)