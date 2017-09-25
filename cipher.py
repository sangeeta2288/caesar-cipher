# ---------- PROBLEM : CAESAR'S CIPHER ----------
# Receive a message and then encrypt it by shifting the
# characters by a requested amount('key' from user) to the right

# Unicodes: A-Z have the numbers 65-90 
# Unicodes: a-z have the numbers 97-122
# You get the unicode of a character with ord(yourLetter)
# You convert from unicode to character with chr(yourNumber)

# Hints
# Use isupper() to decided which unicodes to work with
# Add the key (number of characters to shift) and if
# bigger or smaller then the unicode for A, Z, a, or z
# increase or decrease by 26

message = input(print("Enter your message"))
key = int(input(print("Enter Key(No. to shift each charecter:1-26)")))
print(message)
print(key)
secreat_msg= ""
for char in message:
        if(char.isalpha()):
                char_code = ord(char)
                char_code += key
                
                if(char.isupper()):
                        if(char_code > ord("Z")):
                                char_code-= 26
                        elif(char_code < ord("A")):
                                char_code += 26
                else:
                        if(char_code > ord("z")):
                                char_code-= 26
                        elif(char_code < ord("a")):
                                char_code += 26
                secreat_msg += chr(char_code)
        else:
                secreat_msg += char
        #print(secreat_msg)

print("Encrypted message is: ",secreat_msg)                

