# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        visitedCount = 1
        q = deque([0])

        while q:
            roomNo = q.popleft()
            for key in rooms[roomNo]:
                if not visited[key]:
                    q.append(key)
                    visited[key] = True
                    visitedCount += 1

        return visitedCount == n
