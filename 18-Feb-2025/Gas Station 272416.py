# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        sum_gas,sum_cost = gas[0],cost[0]
        curr_gas = gas[0] - cost[0]
        start_index = 0


        for i in range(1, n):
            if curr_gas < 0:
                start_index = i
                curr_gas = 0
            sum_gas += gas[i]
            sum_cost += cost[i]
            curr_gas += gas[i] - cost[i]

        if sum_gas < sum_cost:
            return -1
            
        return start_index

