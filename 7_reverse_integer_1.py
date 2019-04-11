class Solution:
    def reverse(self, x: int) -> int:
        x=list(str(x))
        neg_bi = int(x[0]=='-')
        num = list(reversed(x[neg_bi:]))
        num = int(''.join(num))
        crit=2**31-1
        if num > crit + neg_bi:
            return 0
        else:
            return (-1)**neg_bi*num