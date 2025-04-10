import concurrent.futures
from hash_utils import hashMd5, reductionFunction, charset, passwordLength

rainbowTableFile = "rainbowTable.txt"
chainLength = 4
threadNum = 8  

def processChain(startPass, endPass, targetHash, chainLen):
   
    currentPass = startPass

    for i in range(chainLen):
        hashValue = hashMd5(currentPass)
        
        if hashValue == targetHash:
            print("[+] Password Recovered!")
            print(f"Plaintext Password: {currentPass}")
            print(f"MD5 Hash: {hashValue}")
            print(f"Reduced Password: {reductionFunction(hashValue, i)}")
            return currentPass, hashValue

        currentPass = reductionFunction(hashValue, i)

    return None  # No match found


def lookUpHash(targetHash, numOfThreads=threadNum):
  
    
    with open(rainbowTableFile, "r") as file:
        chains = [line.strip().split(":") for line in file]

    with concurrent.futures.ThreadPoolExecutor(max_workers=numOfThreads) as executor:
        future_results = {
            executor.submit(processChain, start, end, targetHash, chainLength): start
            for start, end in chains
        }   
        
        for future in concurrent.futures.as_completed(future_results):
            result = future.result()
            if result:
                password, hash_value = result  
                return result  

    print("[-] Password Not Found in Rainbow Table")
    return None


if __name__ == "__main__":
    with open("crackingLog.txt","a") as log:
        
        test_password = "Pass"  # Example password to test
        test_hash = hashMd5(test_password)  # Hash to crack

        log.write(f"\n[*] Looking for hash: {test_hash})")
        print(f"[*] Looking for hash: {test_hash}")
        recovered = lookUpHash(test_hash)

        if recovered:
            log.write(f"\n[+] Successfully cracked: {recovered[0]}")
            print(f"[+] Successfully cracked: {recovered[0]}")
        else:
            log.write("\n[-] Password lookup failed.")
            print("[-] Password lookup failed.")
