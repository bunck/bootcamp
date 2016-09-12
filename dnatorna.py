""" convert DNA seq to RNA"""

def rna(seq):
    """convert DNA seq to RNA"""

    #convert to uppercase
    seq = seq.upper()

    return seq.replace('T', 'U')
