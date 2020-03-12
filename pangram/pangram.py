def is_pangram(sentence):
    lookup = [0] * 26
    sentence = sentence.lower()
    for char in sentence:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            lookup[index] += 1
            
    return all(lookup)
