def encrypt_caesar(sampletext: str,shift: int) -> str:
    result = ""
    for char in sampletext: 
        code = ord(char)
        code = code + shift
        if(code > 90):
            code = code - 26
        nchar = chr(code)
        result += nchar
    return result

def decrypt_caesar(ciphertext: str, shift: int) -> str:
    result = ""
    for char in ciphertext: 
        code = ord(char)
        code = code - shift
        if(code < 65):
            code = code + 26
        nchar = chr(code)
        result += nchar
    return result

print(decrypt_caesar(encrypt_caesar("PYTHON", 6 ),6))