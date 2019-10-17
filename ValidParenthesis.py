def isValid(s):
    '''
    Checks if a given set of paranthesis is valid or not
    '''

    ctr = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = ctr.pop() if ctr else '#'
            if mapping[char] != top_element:
                return False
        else:
            ctr.append(char)
    return not ctr

