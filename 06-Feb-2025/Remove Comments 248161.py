# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        curr_statement = ''
        multiline_comment_started = False
        res = []

        for line in source:
            index = 0
            while index < len(line):
                if multiline_comment_started:
                    if line[index] == '*' and index < len(line) - 1 and line[index + 1] == '/':
                        multiline_comment_started = False
                        index += 1
                    index += 1
                elif line[index] == '/' :
                    if index < len(line) - 1 and line[index + 1] == '*':
                        multiline_comment_started = True
                        index += 1
                    elif index < len(line) - 1 and line[index + 1] == '/':
                        break
                    else:
                        curr_statement += line[index]
                    index += 1
                else:
                    curr_statement += line[index]
                    index += 1
                    
            if curr_statement and not multiline_comment_started:
                res.append(curr_statement)
                curr_statement = ""


        return res
                
