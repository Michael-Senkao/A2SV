# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        roots = set()
        result = []

        folder.sort(key=lambda x: x.count('/'))
        
        for f in folder:
            sub_folder = []
            i = 0
            while i < len(f):
                temp = [f[i], f[i+1]]
                
                i += 2
                while i < len(f) and f[i] != '/':
                    temp.append(f[i])
                    i += 1
                    
                sub_folder.append("".join(temp))
                if tuple(sub_folder) in roots:
                    break
            else:
                roots.add(tuple(sub_folder))

        return ["".join(root) for root in roots]
        