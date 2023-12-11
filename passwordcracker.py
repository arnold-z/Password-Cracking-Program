import threading
import hashlib
import bcrypt
import sys
import os
from itertools import product


# A list of characters that can be used in the password
chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                 "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4",
                 "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]


# Gets user's current working directory to access the file path of the 10k common passwords text file
# Loads the top 10k most common passwords txt file into a list
current_directory = os.getcwd()

relative_path = r"10-million-password-list-top-10000.txt"

file_path = os.path.join(current_directory, relative_path)

with open(file_path, "r") as file:
    common_passwords = file.readlines()
    common_passwords = [line.strip() for line in common_passwords]



# Calculates all possible combinations of the passwords and puts it into a list
# Compares those combinations to the password to see if combination is correct and tracks total attempts
def brute_force_attack(passwordLength):
    combinations = product(chars, repeat=passwordLength)
    total_tries = 0
    for combo in combinations:
        total_tries += 1
        brute_attempt = "".join(combo)
        if password == brute_attempt:
            print("Your password is: " + brute_attempt)
            print("It took " + str(total_tries) + " attempt(s).")
            break


# Initializes 26 threads so the program can determine what length should be used to calculate possible combinations
# target calls the brute_force_attack()
# args is the length of the password and the parameter of the brute_force_attack() 
def initialize_threads():
    threads = []
    for i in range(1, 26):
        thread = threading.Thread(target=brute_force_attack, args=[i])
        threads.append(thread)

    # Start threads
    for thread in threads:
        thread.start()
 
    # Join threads
    for thread in threads:
        thread.join()


# Traverses through the top 10k common password list
# Tries each index and compares it to actual password
def dictionary_attack():
    totalTries = 0
    password_not_found = True
    for i in range(len(common_passwords)):
        totalTries += 1
        if password == common_passwords[i]:
            print("The password is: " + common_passwords[i])
            print("It took " + str(totalTries) + " tries.")
            password_not_found = False
            break
    if password_not_found:
        print("Password not in dictionary.")


# Calls the hashmd5 function
# Checks each hash in the md5_hashes list and compares it to password         
def dictionarymd5_attack():
    hashmd5()
    total_tries = 0
    password_not_found = True
    for i in range(len(password_md5hash_combo)):
        total_tries += 1
        if password == md5_hashes[i]:
            print("The password is: " + password_md5hash_combo[md5_hashes[i]])
            print("It took " + str(total_tries) + " tries.")
            password_not_found = False
            break
    if password_not_found:
        print("Password not in dictionary.")


# Calls the hashsha256 function
# Checks each hash in the sha256_hashes list and compares to the password            
def dictionarysha_attack():
    hashsha256()
    total_tries = 0
    password_not_found = True
    for i in range(len(password_sha256hash_combo)):
        total_tries += 1
        if password == sha256_hashes[i]:
            print("The password is: " + password_sha256hash_combo[sha256_hashes[i]])
            print("It took " + str(total_tries) + " tries.")
            password_not_found = False
            break
    if password_not_found:
        print("Password not in dictionary.")


# Calls the hashbcrypt function
# Uses .checkpw() function to compare user hash to password in common_passwords list      
def dictionarybcrypt_attack():
    hashbcrypt()
    total_tries = 0
    password_not_found = True
    for i in range(len(common_passwords)):
        total_tries += 1
        if bcrypt.checkpw(common_passwords[i].encode('utf-8'), password.encode('utf-8')):
            print("The password is: " + common_passwords[i])
            print("It took " + str(total_tries) + " tries.")
            break
    if password_not_found:
        print("Password not in dictionary.")
        

# Uses product() function to calculate all possible combinations
# Converts each combination to md5 hash and compares it to actual password                   
def brutemd5_attack():
    hashmd5()
    combinations = product(chars, repeat=32)
    total_tries = 0
    for combo in combinations:
        combo_str = "".join(combo)
        combo_hash = hashlib.md5(combo_str.encode('utf-8')).hexdigest()
        total_tries += 1
        if password == combo_hash:
            print("The password is: " + combo_str)
            print("It took " + str(total_tries) + " tries.")
            break


# Uses product() function to calculate all possible combinations
# Converts each combination to sha256 hash and compares it to actual password
def brutesha_attack():
    hashsha256()
    combinations = product(chars, repeat=64)
    total_tries = 0
    for combo in combinations:
        combo_str = "".join(combo)
        combo_hash = hashlib.sha256(combo_str.encode('utf-8')).hexdigest()
        total_tries += 1
        if password == combo_hash:
            print("The password is: " + combo_str)
            print("It took " + str(total_tries) + " tries.")
            break

# Uses product() function to calculate all possible combinations
# Converts each combination to bcrypt hash and compares it to actual password
def brutebcrypt_attack():
    hashbcrypt()
    combinations = product(chars, repeat=60)
    total_tries = 0
    for combo in combinations:
        combo_str = "".join(combo)
        total_tries += 1
        if bcrypt.checkpw(combo_str.encode('utf-8'), password.encode('utf-8')):
            print("The password is: " + combo_str)
            print("It took " + str(total_tries) + " tries.")
            break

        
# Dictionary to map the password to hash combo
password_md5hash_combo = {}

password_sha256hash_combo = {}

password_bcrypthash_combo = {}


# Stores all the hashes in corresponding order with original password
md5_hashes = []

bcrypt_hashes = []

sha256_hashes = []


# Hashes all passwords in common_passwords list 
# Adds the hash to password_md5_hash_combo dictionary and pairs it to the corresponding password
# Also adds to md5_hashes list
def hashmd5():
    for i in range(len(common_passwords)):
        md5_hash = hashlib.md5(str(common_passwords[i]).encode('utf-8'))
        md5_hash = md5_hash.hexdigest()
        password_md5hash_combo[md5_hash] = common_passwords[i]
        md5_hashes.append(md5_hash)


# Hashes all passwords in common_passwords list
# Adds the hash to password_sha256hash_combo dictionary and pairs it to the corresponding password
# Also adds to sha256_hashes list
def hashsha256():
    for i in range(len(common_passwords)): 
        sha256_hash = hashlib.sha256(str(common_passwords[i]).encode("utf-8"))
        sha256_hash = sha256_hash.hexdigest()
        password_sha256hash_combo[sha256_hash] = common_passwords[i]
        sha256_hashes.append(sha256_hash)


# Hashes all passwords in common_passwords list
# Adds the hash to password_bcrypthash_combo dictionary and pairs it to the corresponding password
# Also adds to bcrypt_hashes list
def hashbcrypt():
    for i in range(len(common_passwords)):
        bcrypt_hash = bcrypt.hashpw(str(common_passwords[i]).encode('utf-8'), bcrypt.gensalt())
        password_bcrypthash_combo[bcrypt_hash] = common_passwords[i]
        bcrypt_hashes.append(bcrypt_hash)


# Sets password according to the user's input
password = sys.argv[2] 


# Checks user arguments to decide which function to run
if sys.argv[1] == "-b":
    initialize_threads()
if sys.argv[1] == "-d":
    dictionary_attack()
if sys.argv[1] == "-dm":
    dictionarymd5_attack()
if sys.argv[1] == "-ds":
    dictionarysha_attack()
if sys.argv[1] == "-dbc":
    dictionarybcrypt_attack()
if sys.argv[1] == "-bm":
    brutemd5_attack()
if sys.argv[1] == "-bs":
    brutesha_attack()
if sys.argv[1] == "-bbc":
    brutebcrypt_attack()
