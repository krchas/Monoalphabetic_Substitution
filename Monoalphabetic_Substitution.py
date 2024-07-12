import string
import itertools

def load_word1():
    with open('word1.txt', 'r') as f:
        word1 = f.read().split()
    return set(word1)

def load_cipher_text():
    with open('cipher.txt', 'r') as f:
        cipher_text = f.read()
    return cipher_text

def get_letter_frequency(text):                    #   frequncy : 'a': 2, 'b': 18, 'c': 37 ...
    letter_frequency = {}
    for letter in string.ascii_lowercase:
        letter_frequency[letter] = text.count(letter)
    return letter_frequency
  
def guess_key3(cipher_text, word1):                                 #3
    letter_frequency = get_letter_frequency(cipher_text.lower())
    #excluded_letters = [letter for letter in letter_frequency.keys() if letter_frequency[letter] == 0]
    sorted_letters = sorted([letter for letter in letter_frequency.keys() if letter_frequency[letter] > 0], key=lambda x: letter_frequency[x], reverse=True)
    #print("Excluded letters:", excluded_letters)
    #print()
    f1 = ['n', 'i', 't', 'h', 'o', 'f', 'a']
    f2 = ['s', 'l', 'c', 'r']   
    f3 = ['u', 'p', 'm', 'd']           
    f4 = ['g', 'b', 'y']
    f5 = ['v', 'w', 'k']
    f6 = ['x', 'z', 'q', 'j']
    m_mf = f2 + f3 + f4 + f5 + f6
    key0 = {sorted_letters[0]: 'e'}
    key = check3(cipher_text, word1, sorted_letters, m_mf, f1, key0)
    return key

def check3(cipher_text, word1, sorted_letters, m_mf, f1, key0):
    k2 = 0
    keyf0 = {}
    for perm_f1 in itertools.permutations(sorted_letters[1:8]):
        keyf = dict(zip(perm_f1,f1))
        key0.update(keyf)
        i = 0
        while len(key0) < len(sorted_letters):
             key0.update({sorted_letters[i+8] : m_mf[i]})
             i+=1
        decrypted_text = decrypt(cipher_text, key0)
        k1 = is_plaintext1(decrypted_text, word1)
        if k1 > k2:
            k2 =k1
            keyf0.update(key0)
        key0 = {sorted_letters[0]: 'e'}

    return keyf0

def is_plaintext1(text, word1):
    words_found = 0
    for word in text.split():
        if word.lower() in word1:
            words_found += 10
    return (words_found / len(text.split()))

def decrypt(cipher_text, key):
    mapping_dict = str.maketrans(key)
    return cipher_text.translate(mapping_dict)
