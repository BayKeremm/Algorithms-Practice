from string import ascii_letters
import json

def encrypt(str_input,shift):
    alphabet = ascii_letters
    result = ""
    for char in str_input:
        if char not in alphabet:
            result+=char
        else:
            new_index = alphabet.index(char)+shift
            result+=alphabet[new_index%len(alphabet)]
    return result

def decrypt(str_input,shift):
    shift*=-1
    return encrypt(str_input,shift)

def brute_force(str_input):
    alphabet = ascii_letters
    data = {}
    for shift in range(1,len(alphabet)+1):
        data[shift]=decrypt(str_input,shift)
    return data

if __name__ == "__main__":
    res = encrypt('A very large key', 8000)
    dic=brute_force(res) 
    print(json.dumps(dic,indent=4))

    
