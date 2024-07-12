from Monoalphabetic_Substitution import  load_word1
from Monoalphabetic_Substitution import  load_cipher_text
from Monoalphabetic_Substitution import  get_letter_frequency
from Monoalphabetic_Substitution import  guess_key3
from Monoalphabetic_Substitution import  decrypt

if __name__ == '__main__':
    word1 = load_word1()
    cipher_text = load_cipher_text()

    key = guess_key3(cipher_text, word1)
    decrypted_text = decrypt(cipher_text, key)
    #以上，获得大致的key

    #以下，修正key
    while(1):    
        print()
        print("cipher_text:", cipher_text)
        print()
        print("letter_frequency:", get_letter_frequency(cipher_text.lower()))
        print()
        print("key:",key)
        print()
        print("decrypted_text:",decrypted_text)
        print()
        exkey_str = input("Please supplement the keyword, or fix it (input example:{'n': e, 'a': 'b'}): ")
        key.update(eval(exkey_str))
        decrypted_text = decrypt(cipher_text, key)
        

