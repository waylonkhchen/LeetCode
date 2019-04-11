# Strings J = types of stones that are jewels
# String S = stones you have
# Input
# J = "aA", S = "aAAbbbb"
# Output
# 3
# create a dictionary where the key is the char and
#the value is the number of occurrences

def jewels(S,J):
    #dict is a DICTONARY where each element is keys from J
    #with values 0
    dict = {x: 0 for x in J};
    print (dict)
    for char in S:
        print (char)
        if char in J:
            dict[char] += 1

    return dict
J = "aZAb"
S = "aAAizbbbbc"
print(jewels(S,J))
