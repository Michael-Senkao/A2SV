# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        skillSum = skill[0] + skill[-1]

        chemistrySum = 0
        left,right = 0, len(skill) - 1
        while left < right:
            if skill[left] + skill[right] != skillSum:
                return -1
            chemistrySum += skill[left]*skill[right]
            left += 1
            right -= 1


        return chemistrySum

        