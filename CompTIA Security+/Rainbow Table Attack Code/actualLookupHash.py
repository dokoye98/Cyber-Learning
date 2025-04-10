import concurrent.futures
from hash_utils import hashMd5, reductionFunction, charset, passwordLength

rainbowTableFile = "rainbowTable.txt"
chainLength = 5
threadNum = 6  

def reverseLookup(targetHash):
    """
    Reverse lookup: Compare the hashed value against the reduced values
    to find the plaintext password.
    """
    with open(rainbowTableFile, "r") as file:
        table_entries = [line.strip().split(":") for line in file]

    for startPass, endPass in table_entries:
        currentPass = startPass  

        for i in range(chainLength):
            generatedHash = hashMd5(currentPass)

            if generatedHash == targetHash:
                print(f"[+] Password Found: {currentPass}")
                print(f"[+] Matching Hash: {generatedHash}")
                return currentPass  

            currentPass = reductionFunction(generatedHash, i)

    print("[-] Password Not Found in Rainbow Table")
    return None


if __name__ == "__main__":
    test_password = "pass"
    test_hash = hashMd5(test_password)

    print(f"[+] Looking for hash: {test_hash} (corresponding to '{test_password}')")
    found_password = reverseLookup(test_hash)

    if found_password:
        print(f"[+] Successfully cracked: {found_password}")
    else:
        print("[-] Password lookup failed.")
