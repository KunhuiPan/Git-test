# Problem Set 4A
# Name: <Kunhui Pan>
# Collaborators: None
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    # >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    n = len(sequence)
    results = [] # track and collect result
    if n == 1: # if the length of sequence equals to 1, just return the list of this sequence.
        return [sequence]
    else: # otherwise, divide the sequence into two parts: the first character and the remaining, then get the permutations of the remaining characters, then add them together.
        for count, value in enumerate(sequence): # get index and element of the sequence at the same time
            results += [value+item for item in get_permutations(sequence[:count] + sequence[count+1:])]
        return results

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input1 = "abc"
    print("Input: ", example_input1)
    print("Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']")
    expected_output1 = get_permutations(example_input1)
    print("Actual Output: ", expected_output1)
    print("_________________________")
    example_input2 = "use"
    print("Input: ", example_input2)
    print("Expected Output: ['use', 'ues', 'sue', 'seu', 'eus', 'esu']")
    expected_output2 = get_permutations(example_input2)
    print("Actual Output: ", expected_output2)
    print("_________________________")
    example_input3 = "are"
    print("Input: ", example_input3)
    print("Expected Output: ['are', 'are', 'rae', 'bea', 'ear', 'era']")
    expected_output3 = get_permutations(example_input3)
    print("Actual Output: ", expected_output3)

    print("test", get_permutations("aeiou"),len(get_permutations("aeiou")))
