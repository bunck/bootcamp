openp = ''
closedp = ''
def parentheses_counter(s1):
    openp = s1.count('(')
    closedp = s1.count(')')

    if openp == closedp:
        print ('they match')
    elif openp != closedp:
        print ('no match')
    else:
        print ('Other problem')

def dotparen_to_bp('(((...)))')
