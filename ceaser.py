def encrypt_ceasar(sampletext: str) -> str:
    result = ""
    for char in sampletext: 
        code = ord(char)
        code = code + 3
        if(code > 90):
            code = code - 26
        nchar = chr(code)
        result += nchar
    return result

def decrypt_caesar(ciphertext: str) -> str:
    result = ""
    for char in ciphertext: 
        code = ord(char)
        code = code - 3
        if(code < 65):
            code = code + 26
        nchar = chr(code)
        result += nchar
    return result

print(decrypt_caesar("SBWKRQ"))
