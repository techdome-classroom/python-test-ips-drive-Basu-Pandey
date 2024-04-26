def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    pass
n = len(s)
    if n == 0:
        return 0

    max_length = 0
    start = 0
    char_index_map = {}

    for end in range(n):
        if s[end] in char_index_map:
            
            start = max(start, char_index_map[s[end]] + 1)
        
       
        char_index_map[s[end]] = end
        
        
        max_length = max(max_length, end - start + 1)
    
    return max_lengt


