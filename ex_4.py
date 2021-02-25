# by Kami Bigdely
# Replace nested conditional with gaurd clauses

def extract_position(line):
    if 'x:' in line:
        start_index = line.find('x:') + 2
        pos = line[start_index:] # from start_index to the end.
    else: 
        pos = None
    return pos

def test_extract_position():
    res1 = extract_position("")
    assert res1 == None

    res2 = extract_position("x:16.92")
    assert res2 == "16.92"
    
    res3 = extract_position("|error|")
    assert res3 == None

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)