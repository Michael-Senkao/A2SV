# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

from collections import deque

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        
        q = deque()
        visited = set()

        q.append(id)
        visited.add(id)

        while q and level > 0:
            for _ in range(len(q)):
                person = q.popleft()
                for friend in friends[person]:
                    if friend not in visited:
                        q.append(friend)
                        visited.add(friend)
            level -= 1

        videosFreq = defaultdict(int)
        for person in q:
            for video in watchedVideos[person]:
                videosFreq[video] += 1
        return sorted(videosFreq.keys(), key=lambda key: (videosFreq[key], key))
        