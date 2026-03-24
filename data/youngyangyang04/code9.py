class Solution:
    def climbStairs(self, n):
        if n is not None:
            if n > 0:
                if n == 1:
                    return 1
                else:
                    if n == 2:
                        return 2
                    else:
                        a = 1
                        b = 2
                        i = 3
                        while i <= n:
                            if i > 2:
                                c = a + b
                                if c > 0:
                                    a = b
                                    b = c
                            i += 1
                        return b
            else:
                return 0
        else:
            return 0
