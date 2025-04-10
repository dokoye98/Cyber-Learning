from hash_utils import hashMd5, reductionFunction

test_password = "admin1"
hashed = hashMd5(test_password)
reduced = reductionFunction(hashed, 1)

print(f"Original Password: {test_password}")
print(f"MD5 Hash: {hashed}")
print(f"Reduced Password: {reduced}")
