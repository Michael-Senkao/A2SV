# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        min_cost = 0
        a_indices,b_indices = [],[]
        
        
        for index, (a,b) in enumerate(costs):
            if a > b:
                b_indices.append(index)
            else:
                a_indices.append(index)

        # Check if city A has more cheaper costs than city B
        if len(a_indices) > len(b_indices):
           
            # Sort costs of city A by the change in travel cost
            a_indices.sort(key=lambda i: costs[i][1] - costs[i][0], reverse = True)
            
            # Add the people with smaller change in travel cost to city B until the size is equal
            while len(a_indices) > len(b_indices):
                b_indices.append(a_indices.pop())
        elif len(b_indices) > len(a_indices): # Check if city A has more cheaper costs than city B
            
            # Sort costs of city B by the change in travel cost
            b_indices.sort(key=lambda i: costs[i][0] - costs[i][1], reverse = True)
            
            # Add the people with smaller change in travel cost to city A until the size is equal
            while len(b_indices) > len(a_indices):
                a_indices.append(b_indices.pop())

        # Calculate the minimum travel cost for each city
        for i in range(n):
            min_cost += costs[a_indices[i]][0]
            min_cost += costs[b_indices[i]][1]
            
        return min_cost
        