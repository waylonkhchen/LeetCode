class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import string
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet= list(string.ascii_lowercase)
        dictionary=dict(zip(alphabet,morseCode))
        ###print('dictionary is \n', dictionary, '\n')

        morsecode_wds =[];
        for x in words: #ex. x='cool'
            #break each element in words into a list of individual letters
            string=list(x); #eg.string = ['c','o','o','l']
            ###print('string is',string);

            #morsecode_str_ls stores the morse_code of each string
            morsecode_str_ls=[];

            for i in string: #eg. i=c, i=o,...
                #concatenate morsecode of each string
                morsecode_str_ls += dictionary[i];
                ###print(morsecode_str_ls)

            #join the string list of morse_code into a single string
            morsecode_str = ''.join(morsecode_str_ls)
            ###print('morsecode_str is : ',morsecode_str)


            #append new morse_code string
            morsecode_wds.append(morsecode_str)
            ###print('morsecode_wds is : ',morsecode_wds)

        #reduce the list to a set that remove the duplicates
        red_morsecode_wds = list(set(morsecode_wds))
        #return the length of the reduced list being the number of uniques MorseCodes
        return len(red_morsecode_wds)
