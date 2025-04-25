# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = list(filter(lambda dir: dir!='', path.split('/')))
        stack = []
       
        for dir in directories:
            if dir == '..':
                if stack:
                    stack.pop()
            elif dir != '.':
                stack.append(dir)

        return '/'+'/'.join(stack)