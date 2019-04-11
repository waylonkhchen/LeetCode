class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict = {x: 0 for x in J};

        for char in S:
            if char in J:
                dict[char] += 1
        return sum(dict.values())
