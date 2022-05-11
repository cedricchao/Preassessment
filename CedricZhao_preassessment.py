def lengthLongestSubstring(s):
    '''
    :param s: a string
    :return: the length of the longest substring without repeating characters.
    '''
    assert isinstance(s, str) 
    assert 0 <= len(s) <= 5 * (10**4)
    
    subString = ''
    res = 0
    for char in s:
        if char not in subString:
            subString += char
            res = max(len(subString), res)
        else:
            subString = subString[subString.index(char)+1:]+char
    return res
if __name__ == '__main__':
    s1 = "abcabcbb" 
    print(lengthLongestSubstring(s1))
    s2 = "bbbbb"
    print(lengthLongestSubstring(s2))
    s3 = "pwwkew" 
    print(lengthLongestSubstring(s3))
    s4 = "abcdefgh" 
    print(lengthLongestSubstring(s4))
    s5 = "abeabcd" 
    print(lengthLongestSubstring(s5))
    s6 = "pww+++++ kew +++abcd+e-2" 
    print(lengthLongestSubstring(s6))
