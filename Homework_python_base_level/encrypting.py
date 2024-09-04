text = "I encrypted this text and I say hello to everyone who could read it and you are great"
dictionary = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! '


# ENCODE Text
def encode_text(input_text):
    shift_left, shift_right = 28, 12
    secret_text = ""

    for char in range(len(input_text)):
        index = dictionary.index(input_text[char])
        if char % 2 == 0:
            new_pos = (index - shift_right + len(dictionary)) % len(dictionary)
        else:
            new_pos = (index + shift_left + len(dictionary)) % len(dictionary)
        secret_text += dictionary[new_pos]
    return secret_text


encoded_result = encode_text(text)
print(encoded_result)


# DECODE Text
def decode_text(encoded_text):
    shift_left, shift_right = 28, 12
    secret_text = ""

    for char in range(len(encoded_text)):
        index = dictionary.index(encoded_text[char])
        if char % 2 == 0:
            new_pos = (index + shift_right + len(dictionary)) % len(dictionary)
        else:
            new_pos = (index - shift_left + len(dictionary)) % len(dictionary)
        secret_text += dictionary[new_pos]
    return secret_text


decoded_result = decode_text(encoded_result)
print(f"А этот текст мы расшифровали:\n {decoded_result}")
