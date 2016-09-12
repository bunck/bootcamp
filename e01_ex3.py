def complement_base(base, material='DNA'):
    """return watson crick complement of a base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq, material):
    """compute reverse complement of a nucleic acid sequence"""

    # initialize empty string
    rev_comp = ''
    seq_rev = seq[::-1]
    # loop through and add new rev comp bases
    for base in seq_rev:
        rev_comp += complement_base(base, material=material)

    return rev_comp
