def ratio(x, y):
    """The ratio of 'x' to 'y'."""
    return x / y

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

    # loop through and add new rev comp bases
    for base in reversed(seq):
        rev_comp += complement_base(base, material=material)

    return rev_comp

def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """simpler program that deep thoughts, i bet"""
    return 42

def think_too_much():
    """express ceasar's skepticism about cassius"""

    print("""Yond Cassius has a lean and hungry look,
    He thinks too much""")
