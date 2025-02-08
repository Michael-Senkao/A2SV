# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomains_count = defaultdict(int)
        result = []

        for cpdomain in cpdomains:
            count, subdomain = cpdomain.split()
            count = int(count)

            while len(subdomain) > 0:
                subdomains_count[subdomain] += count
                parent_start_index = subdomain.find('.') + 1
                if parent_start_index == 0:
                    break
                subdomain = subdomain[parent_start_index: ]

        for subdomain, count in subdomains_count.items():
            result.append(str(count) + " " + subdomain)
        return result
                