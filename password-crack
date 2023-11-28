import threading
from itertools import product

# A list of characters that can be used in the password
chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                 "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4",
                 "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

# Asks the user to create their password
password = input("Enter your desired password (0-26 letters): ")

# Calculates all possible combinations of the passwords and puts it into a list
# Compares those combinations to the password to see if combination is correct and tracks total attempts
def guessFunction(passwordLength):
    combinations = product(chars, repeat=passwordLength)
    totalTries = 0
    for combo in combinations:
        totalTries += 1
        if password == "".join(combo):
            print("Your password is: " + password)
            print("It took " + str(totalTries) + " attempt(s).")
            
    
# Initializes 26 threads so the program can determine what length should be used to calculate possible combinations
# target calls the guessFunction()
# args is the length of the password and the parameter of the guessFunction() 
t1 = threading.Thread(target=guessFunction, args=(1,))
t2 = threading.Thread(target=guessFunction, args=(2,))
t3 = threading.Thread(target=guessFunction, args=(3,))
t4 = threading.Thread(target=guessFunction, args=(4,))
t5 = threading.Thread(target=guessFunction, args=(5,))
t6 = threading.Thread(target=guessFunction, args=(6,))
t7 = threading.Thread(target=guessFunction, args=(7,))
t8 = threading.Thread(target=guessFunction, args=(8,))
t9 = threading.Thread(target=guessFunction, args=(9,))
t10 = threading.Thread(target=guessFunction, args=(10,))
t11 = threading.Thread(target=guessFunction, args=(11,))
t12 = threading.Thread(target=guessFunction, args=(12,))
t13 = threading.Thread(target=guessFunction, args=(13,))
t14 = threading.Thread(target=guessFunction, args=(14,))
t15 = threading.Thread(target=guessFunction, args=(15,))
t16 = threading.Thread(target=guessFunction, args=(16,))
t17 = threading.Thread(target=guessFunction, args=(17,))
t18 = threading.Thread(target=guessFunction, args=(18,))
t19 = threading.Thread(target=guessFunction, args=(19,))
t20 = threading.Thread(target=guessFunction, args=(20,))
t21 = threading.Thread(target=guessFunction, args=(21,))
t22 = threading.Thread(target=guessFunction, args=(22,))
t23 = threading.Thread(target=guessFunction, args=(23,))
t24 = threading.Thread(target=guessFunction, args=(24,))
t25 = threading.Thread(target=guessFunction, args=(25,))
t26 = threading.Thread(target=guessFunction, args=(26,))

# Starts the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()
t19.start()
t20.start()
t21.start()
t22.start()
t23.start()
t24.start()
t25.start()
t26.start()

# Ends the threads 
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
t14.join()
t15.join()
t16.join()
t17.join()
t18.join()
t19.join()
t20.join()
t21.join()
t22.join()
t23.join()
t24.join()
t25.join()
t26.join()
