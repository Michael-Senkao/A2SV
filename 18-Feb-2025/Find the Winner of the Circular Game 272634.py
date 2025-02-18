# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Number of each palyer initially
        queue = deque([i for i in range(1, n + 1)])

        # Player to be removed is k - 1 since the array 0-indexed
        k = k - 1

        while len(queue) > 1:
            # Get index of player to be removed
            remove_index = k % len(queue)

            if remove_index == len(queue) - 1: # Player is at last index
                queue.pop()
            else:
                # Pop all elements that come before the player to remove
                # and add it to the end of the queue
                for _ in range(remove_index):
                    queue.append(queue.popleft())

                # Pop the player to be removed
                queue.popleft()
                
           

        return queue[0] # 