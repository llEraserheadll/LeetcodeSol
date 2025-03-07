class Solution:
    def isHappy(self, n: int) -> bool:
        def square_of_digits(number):
            total_sum = 0
            while number > 0:
                number,digit = divmod(number,10)
                total_sum += digit **2
            return total_sum
        
        slow_pointer = n
        fast_pointer = square_of_digits(n)

        while fast_pointer != 1 and slow_pointer != fast_pointer:
            slow_pointer = square_of_digits(slow_pointer)
            fast_pointer = square_of_digits(square_of_digits(fast_pointer))

        if fast_pointer == 1:
            return True
        return False
        