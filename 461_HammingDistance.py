class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #x_bin store x in a 33 digit binary string of 0/1
        x_bin=format(x,'033b');
        y_bin=format(y,'033b');

        #x_intList stores the int list of the string x_bin
        x_intList=list(map(int,x_bin));
        y_intList=list(map(int,y_bin));

        #x_bool convert the 1/0 list into a Boolean list
        #x_bool = list(map(bool,x_intList));
        #y_bool = list(map(bool,y_intList));
        #note that converting x_bin directly to bool doesn't work
        #since elements in x_bin are not integers

        #length = len(x_intList);
        result_bool = map(add,x_intList,y_intLIst);
        result_bool = map(%2,result_bool);
        #for i in range(length):
        #    result_bool.append((x_intList[i] + y_intList[i])%2)
        return sum(result_bool)
