def permutations(elements):
    
    if len(elements) == 1:
        result = elements
        
    else:
        result = []
        for element in elements:
            
            other_elements = elements.copy()
            other_elements.remove(element)
            
            other_permutations = permutations(other_elements)
            
            for permutation in other_permutations:
                result.append(element + permutation)
            
    return result
