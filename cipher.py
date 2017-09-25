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
