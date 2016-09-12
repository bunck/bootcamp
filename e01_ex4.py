#longest common substring, Ex1 Problem 4

#sequence shortener
#def shorten (seq1):
    #print(seq1)
    #seq2 = seq1.replace(seq1[0],"",1)
    #print(seq2)


    #seq2 = seq2.replace(seq2[0],"",1)
    #return seq2

def shorten (s1, s2):
    longest = ''
    for i in range(len(s1)):
        for j in range(len(s1)):
            s = s1[i:j]
            if s2.count(s) > 0 and len(s) > len(longest):
                longest = s
    return longest
