# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    
        remaining_asteroids = []  # Stack to store the state of asteroids after collisions

        for asteroid in asteroids:
            if asteroid > 0:
                # Right-moving asteroid, no immediate collision, add to stack
                remaining_asteroids.append(asteroid)
            else:
                # Left-moving asteroid, check for collisions with right-moving asteroids
                while remaining_asteroids and remaining_asteroids[-1] > 0 and remaining_asteroids[-1] < -asteroid:
                    # The top right-moving asteroid is smaller, so it gets destroyed
                    remaining_asteroids.pop()
                
                if not remaining_asteroids or remaining_asteroids[-1] < 0:
                    # If no collision occurs or the top asteroid is also left-moving, add to stack
                    remaining_asteroids.append(asteroid)
                elif remaining_asteroids[-1] == -asteroid:
                    # Equal-sized asteroids annihilate each other
                    remaining_asteroids.pop()

        return remaining_asteroids
