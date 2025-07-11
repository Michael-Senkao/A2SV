# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        # Map each task to it's index
        tasks_to_indx = [[enque,proc, indx] for indx, (enque, proc) in enumerate(tasks)]
        tasks_to_indx.sort() # Sort the mapped tasks in order of their enque time
        min_heap = []
        res = []
        
        time = 0
        indx = 0
        # Go through the sorted tasks
        while indx < n:
            
            # Adjust the current time to be atleast the enque time of current task
            if time < tasks_to_indx[indx][0] and not min_heap:
                time = max(time, tasks_to_indx[indx][0])
            # Add all tasks that has enque time less than or equal to the current time (already in queue)
            while indx < n and tasks_to_indx[indx][0] <= time:
                heapq.heappush(min_heap, tuple(tasks_to_indx[indx][1:]))
                indx += 1
            # Take the task with the minimum processing time among all the enqueued tasks
            res.append(min_heap[0][1]) 
            time += min_heap[0][0] # Update the current time 
            heapq.heappop(min_heap) # Process the smallest task

        # Process the rest of the tasks in the queue according to their processing time
        while min_heap:
            res.append(min_heap[0][1])
            heapq.heappop(min_heap)
        
        return res