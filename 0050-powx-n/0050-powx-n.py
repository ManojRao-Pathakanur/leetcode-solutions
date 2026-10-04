class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)
        ans = 1.0
        
        while N > 0:
            if N % 2 == 1:
                ans *= x
            x *= x
            N //= 2
            
        return 1.0 / ans if n < 0 else ans