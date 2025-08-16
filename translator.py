import random

# Mapping: a=1, b=2 ... z=26
alphabet_map = {chr(i + 96): str(i) for i in range(1, 27)}
reverse_map = {v: k for k, v in alphabet_map.items()}

# Possible separators for letters
letter_separators = ["-", ".", ":"]

def encode(text):
    """Encode normal text into custom language"""
    encoded_sentence = []
    words = text.lower().split(" ")
    
    for word in words:
        encoded_word = ""
        for char in word:
            if char in alphabet_map:
                # Pick a random separator for fun
                sep = random.choice(letter_separators)
                encoded_word += alphabet_map[char] + sep
        encoded_sentence.append(encoded_word.strip("".join(letter_separators)))
    
    return "_".join(encoded_sentence) + ";"


def decode(code):
    """Decode custom language back to normal text"""
    words = code.strip(";").split("_")
    decoded_sentence = []
    
    for word in words:
        decoded_word = ""
        # split by all separators
        letters = []
        temp = ""
        for ch in word:
            if ch.isdigit():
                temp += ch
            else:
                if temp != "":
                    letters.append(temp)
                    temp = ""
        if temp != "":
            letters.append(temp)

        for num in letters:
            if num in reverse_map:
                decoded_word += reverse_map[num]
        decoded_sentence.append(decoded_word)
    
    return " ".join(decoded_sentence)


# --------------------------
# DEMO
# --------------------------
text = "hello world"
encoded = encode(text)
decoded = decode(encoded)

print("Original:", text)
print("Encoded :", encoded)
print("Decoded :", decoded)
