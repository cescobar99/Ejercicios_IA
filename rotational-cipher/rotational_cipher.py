def rotate(text, key):
    code = []

    for letter in text:
        if letter.isupper():
          new_letter = (ord(letter) + key) % 91

          if new_letter < 65: new_letter = chr(new_letter + 65)
          else:               new_letter = chr(new_letter)

          code.append(new_letter)
        elif letter.islower():
          new_letter = (ord(letter) + key) % 123

          if new_letter < 97: new_letter = chr(new_letter + 97)
          else:               new_letter = chr(new_letter)

          code.append(new_letter)
        else:
          code.append(letter)

    return ''.join(code)
