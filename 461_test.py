import numpy as np
x=25;
y=10;
    #convert x into binary string with F-string formatting
    #the formatting syntax:
    #x is the argument to be formatted
    #: is followed by the format options
    #the first 0 fills zeros (instead of blank) in front of the binary representation
    #33 specifies the desire length of the formatted string
x_bin=format(x,'033b');
y_bin=format(y,'033b');

#x_bin = f'{x:033b}';
#_bin = f'{y:033b}';

    #convert x_bin to numpy array of dtype= int 0/1 only
    #convert x_npa to boolean (0/1 -> T/F)
x_npa=np.array(list(x_bin),dtype=int);
x_bool = list(map(bool,x_npa));
y_npa=np.array(list(y_bin),dtype=int);
y_bool = list(map(bool,y_npa));

    #find the np.logical_xor of the two boolean array
result_bool = np.logical_xor(x_bool, y_bool);
    #1*x convert x form boolean to 0/1
result_bool = 1*result_bool;
    #sum the result_bool to find the return value

#        print(sum(result_bool))
print(x_npa,'\n')
print(y_npa,'\n')
print(sum(result_bool))
