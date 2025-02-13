# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.nums_count = defaultdict(int)
        self.freq_count = defaultdict(int)

    def add(self, number: int) -> None:
        prev_count = self.nums_count.get(number, 0)
        self.nums_count[number] = prev_count + 1
        self.freq_count[prev_count + 1] += 1

        if prev_count:
            self.freq_count[prev_count] -= 1
            if self.freq_count[prev_count] == 0:
                del self.freq_count[prev_count]

        


    def deleteOne(self, number: int) -> None:
        # Get previous frequency of 'number' if it exists
        prev_count = self.nums_count.get(number, 0)
        if prev_count:
            self.nums_count[number] -= 1 # Decrement the count of 'number' by 1
            self.freq_count[prev_count] -= 1 # Decrement the frequency of 'prev_count' by 1
            # Increment the frequency of the current frequency of 'number' by 1
            self.freq_count[prev_count - 1] += 1

            # Check if there's no number with frequency 'prev_count' and delete the key if True
            if self.freq_count[prev_count] == 0:
                del self.freq_count[prev_count]

        


    def hasFrequency(self, frequency: int) -> bool:
        # Return True if frequency is in the freq_count else False
        return frequency in self.freq_count


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)