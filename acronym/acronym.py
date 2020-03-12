import re

def abbreviate(words):
    new_words = re.findall(r"[A-Za-z\']+(?:\`[A-Za-z]+)?", words)
    new_data = ''
    for word in new_words:
        new_data += word[0]
    return new_data.upper()