
# encryption
def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        c = text[i]

        if c==" ":
            result += " "
            continue
        # if uppercase
        if(c.isupper()):
            result += chr(((ord(c) + s - ord("A")) % 26) + ord("A"))
        
        # if lowercase
        else:
            result += chr(((ord(c) + s - ord("a")) % 26) + ord("a"))
    return result

# decryption
def decrypt(text,s):
    result = ""
    for i in range(len(text)):
        c = text[i]

        if c==" ":
            result += " "
            continue
        # if uppercase
        if(c.isupper()):
            result += chr(((ord(c) - s - ord("A") + 26) % 26) + ord("A"))
        
        # if lowercase
        else:
            result += chr(((ord(c) - s - ord("a") + 26) % 26) + ord("a"))
    return result

text = input("Enter Plain Text: ")
s = int(input("Enter key value: "))
cipher = encrypt(text,s)
print("Cipher Text: ", cipher)
print("Recovered plain Text: ", decrypt(cipher,s))
