class Solution:
    def hammingDistance(self, x, y):
        diffs = 0;
        str1 = format(x,'033b');
        str2 = format(y,'033b');
        for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                diffs += 1
        return diffs
