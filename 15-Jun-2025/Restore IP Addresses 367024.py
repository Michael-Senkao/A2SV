# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def backtrack(self, index, ip_addr, curr, dots, res, s):
        if int(curr) > 255 or dots > 3:
            return
        if index == len(s):
            
            if dots == 3:
                res.append(ip_addr[1:] + '.' + curr)
            return
        self.backtrack(index + 1, ip_addr + '.' + curr, s[index], dots + 1, res, s)
        if int(curr) != 0:
            self.backtrack(index + 1, ip_addr, curr + s[index], dots, res, s)

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12 or n < 4:
            return []
        

        res = []
        self.backtrack(1, '', s[0], 0, res, s)
        return res