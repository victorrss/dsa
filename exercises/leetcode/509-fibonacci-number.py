class Solution:
    def fib(self, n: int) -> int:
        MAX_N = 31
        array = [0] * MAX_N

        array[0] = 0
        array[1] = 1
        for i in range(2, MAX_N):
            array[i] = array[i - 2] + array[i - 1]

        return array[n]
      
# # Recursive form
# class Solution:
#     def fib(self, n: int) -> int:
#         if n<2:
#             return n
#         return self.fib(n-2) + self.fib(n-1)
