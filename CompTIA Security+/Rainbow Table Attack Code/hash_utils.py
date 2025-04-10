import hashlib
import string


charset = string.ascii_letters + string.digits

passwordLength = 4

def hashMd5(plaintext):
    return hashlib.md5(plaintext.encode()).hexdigest()

def reductionFunction(hashValue, roundNum):
   
    num = int(hashValue[:8], 16) 
    reducedPassword = ""
    
    for _ in range(passwordLength):
        reducedPassword += charset[num % len(charset)]
        num //= len(charset)
    
    return reducedPassword


#inputPassword = "pass"
#hash1 = hashMd5(inputPassword)
#reducedPassword = reductionFunction(hash1,1)

#print(f"Input Password: {inputPassword}")
#print(f"MD5 Hash: {hash1}")
#print(f"Reduced Password: {reducedPassword}")

##MD5 Hash: e00cf25ad42683b3df678c61f42c6bda
##Reduced Password: 2qjyge