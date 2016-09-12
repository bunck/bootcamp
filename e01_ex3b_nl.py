def reverse_complement(seq, material):
    """compute reverse complement of a nucleic acid sequence"""

    # initialize empty string
    seq_rev = seq[::-1]
    seq_rev = seq_rev.replace('A' , 'a')
    seq_rev = seq_rev.replace('T' , 't')
    seq_rev = seq_rev.replace('G' , 'g')
    seq_rev = seq_rev.replace('C' , 'c')
    seq_rev = seq_rev.replace('a' , 'T')
    seq_rev = seq_rev.replace('t' , 'A')
    seq_rev = seq_rev.replace('g' , 'C')
    seq_rev = seq_rev.replace('c' , 'G')
    return seq_rev
    #seq_rev.replace('A' , 'T')
    # adding nucleotide
    #rev_comp += complement_base(seq_rev[i], material=material)

    #return rev_comp
