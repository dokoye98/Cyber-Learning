import random
import os
import concurrent.futures
from hash_utils import hashMd5, reductionFunction, charset, passwordLength

rainbowTableFile = "rainbowTable.txt"
passwordDumpFile = "generatedPasswords.txt"
numChains = 1000000  # Number of password chains
chainLength = 5  
numThreads = 8  

def generateRainbowChain(startPass, chainLen=chainLength):
    """Generates a single rainbow chain from a given starting password."""
    currentPass = startPass
    chainSteps = [currentPass]

    for i in range(chainLen):
        hashValue = hashMd5(currentPass)
        currentPass = reductionFunction(hashValue, i)
        chainSteps.append(currentPass)

    return startPass, currentPass, chainSteps


def generateRainbowTableFile():
    
    if os.path.exists(rainbowTableFile):
        os.remove(rainbowTableFile)
        print(f"[-] {rainbowTableFile} has been deleted")

    if os.path.exists(passwordDumpFile):
        os.remove(passwordDumpFile)
        print(f"[-] {passwordDumpFile} has been deleted")

    def worker(_):
        """Worker function to generate a single chain."""
        startPass = "".join(random.choices(charset, k=passwordLength))
        start, end, chainSteps = generateRainbowChain(startPass)
        return f"{start}:{end}", "\n".join(chainSteps)

    with open(rainbowTableFile, "w") as table_file, open(passwordDumpFile, "w") as pass_file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=numThreads) as executor:
            results = list(executor.map(worker, range(numChains)))

        # Write results in bulk to improve performance
        table_entries, password_entries = zip(*results)
        table_file.write("\n".join(table_entries) + "\n")
        pass_file.write("\n".join(password_entries) + "\n")

    print(f"[-] Rainbow Table with {numChains} chains saved to {rainbowTableFile}")
    print(f"[-] Full list of generated passwords saved to {passwordDumpFile}")


if __name__ == "__main__":
    generateRainbowTableFile()
