# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def moveUp(self, curr_x, curr_y, command, obstacles):
        for _ in range(command):
            if (curr_x, curr_y + 1) in obstacles:
                break
            curr_y += 1

        return (curr_x, curr_y)

    def moveRight(self, curr_x, curr_y, command, obstacles):
        for _ in range(command):
            if (curr_x + 1, curr_y) in obstacles:
                break
            curr_x += 1

        return (curr_x, curr_y)

    def moveDown(self, curr_x, curr_y, command, obstacles):
        for _ in range(command):
            if (curr_x, curr_y - 1) in obstacles:
                break
            curr_y -= 1

        return (curr_x, curr_y)

    def moveLeft(self, curr_x, curr_y, command, obsticles):
        for _ in range(command):
            if (curr_x - 1, curr_y) in obsticles:
                break
            curr_x -= 1

        return (curr_x, curr_y)

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {(x,y) for x,y in obstacles}

        curr_x,curr_y = 0,0
        direction = 0
        max_distance = 0

        for command in commands:
            if command == -1:
                _, direction = divmod(direction + 1, 4)
                continue
            elif command == -2:
                _, direction = divmod(direction + 4 - 1, 4)
                continue
            elif direction == 0:
                curr_x, curr_y = self.moveUp(curr_x, curr_y, command, obstacles)
            elif direction == 1:
                curr_x,curr_y = self.moveRight(curr_x, curr_y, command, obstacles)
            elif direction == 2:
                curr_x, curr_y = self.moveDown(curr_x, curr_y, command, obstacles)
            else:
               curr_x, curr_y = self.moveLeft(curr_x, curr_y, command, obstacles) 

            max_distance = max(max_distance, curr_x**2 + curr_y**2)
            
        return max_distance