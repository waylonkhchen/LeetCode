class Solution:
#    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = "aA"; S = "aAAbbbb";
        #jewels is a dictionary
        #such that each element in J is assigned a key zero
        jewels = {x: 0 for x in J}
        print(jewels)

        #Accessing values in dictionary
        print (jewels['a'])
        print (jewels['A'])

        #updating a dictionary
        jewels['a'] =1;
        print('jewels is now %r' %jewels)
        jewels['a'] +=1;
        print('jewels [\'a\'] is now %r' %jewels['a'])

        #delete dictionary elements
        print('now we delete a')
        del jewels['a'];
        print ('jewels is now',jewels)

        print('or we can clear all enetries in a dictionary')
        jewels.clear();
        print('jewels is now', jewels)

        jewels = {x: 0 for x in J};
        jew= jewels.copy()
        print(jew)
        print('keys: %s' %jew.keys())
        print('values: %r' %jew.values())

        print('items:%s'  %jew.items())
