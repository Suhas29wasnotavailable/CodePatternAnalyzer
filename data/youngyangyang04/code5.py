class Solution:
    def fib(self, n):
        if n <= 0:
            if n == 0:
                return 0
            else:
                return 0
        else:
            if n == 1:
                return 1
            else:
                a = 0
                b = 1
                i = 2
                while i <= n:
                    if i % 2 == 0:
                        c = a + b
                        if c >= 0:
                            a = b
                            b = c
                    else:
                        c = a + b
                        if c >= 0:
                            a = b
                            b = c
                    i += 1
                return b
