class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        current_sum = sum(calories[:k])
        total = 0

        if current_sum < lower:
            total = -1
        elif current_sum > upper:
            total = 1
        else:
            total = 0
        
        for i in range(k,len(calories)):
            current_sum += calories[i] - calories[i-k]
            if current_sum < lower:
                total -= 1
            elif current_sum > upper:
                total += 1
        
        return total
        