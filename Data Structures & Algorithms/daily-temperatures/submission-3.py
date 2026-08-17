class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 1, -1, -1):  # ✓ FIX: Start from right
            if i == len(temperatures) - 1:
                continue  # Last day has no warmer day ahead
            
            j = i + 1  # Next day
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if res[j] == 0:  # j has no warmer day, so neither does i
                    break
                j += res[j]  # Jump to the next candidate
            
            if j < len(temperatures) and temperatures[j] > temperatures[i]:
                res[i] = j - i
        
        return res