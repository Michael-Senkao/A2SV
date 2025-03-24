# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        adj_list = defaultdict(list)
        
        for x,y,t in meetings:
            adj_list[x].append((y, t))
            adj_list[y].append((x,t))

        secretTimes = [-1] * n

        minHeap = [(0,0), (0, firstPerson)]
        heapq.heapify(minHeap)

        
        secretTimes[0] = 0
        secretTimes[firstPerson] = 0   

        hasSecret = {0, firstPerson}
        count = 0
        while minHeap:
            secretTime,curr = heapq.heappop(minHeap)
            if secretTime > secretTimes[curr]:
                continue
            count += 1
            for friend, meetingTime in adj_list[curr]:
                if meetingTime >= secretTime:
                    if secretTimes[friend] == -1 or meetingTime < secretTimes[friend]:
                        secretTimes[friend] = meetingTime
                        heapq.heappush(minHeap, (meetingTime,friend))
                        hasSecret.add(friend)
      
        return list(hasSecret)





        return hasSecret

        