# Password Cracking Program 😄

## Dependencies 📦

### threading Library:
```
import threading 
```
- Separates workload onto multiple threads.
- Used to help make brute force attack more efficient.

Read more [here.](https://www.geeksforgeeks.org/multithreading-python-set-1/)


### hashlib Library:
```
import hashlib 
```

- Used to hash passwords with md5 and sha256.
- Hashed passwords are added to lists and dictionaries to store password : dictionary pair.

Read more [here](https://docs.python.org/3/library/hashlib.html) or [here.](https://www.geeksforgeeks.org/hashlib-module-in-python/)


### bcrypt Library:
```
import bcrypt 
```

- Used to hash passwords with bcrypt.
- Checks if user's hash matches with password in dictionary attack.

**MAKE SURE YOU INSTALL BCRYPT BEFORE RUNNING:**

```
pip install bcrypt
```
**If you have trouble with bcrypt installation:**
- Read more [here](https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/) and [here.](https://pypi.org/project/bcrypt/)


### sys library:
```
import sys
```

- Tracks user's arguments in command line
- Runs different functions/programs based on various arguments
- Able to add arguments to program
- Script name is first argument
- Password cracker type is second argument
- Actual user password to crack is third argument

Read more [here](https://www.geeksforgeeks.org/python-sys-module/) or [here.](https://docs.python.org/3/library/sys.html)


### os library:
```
import os
```

- Gets user's current working directory
- Allows for top 10k common password text file to be read by program

Read more [here.](https://docs.python.org/3/library/os.html)


### itertools product library:
```
from itertools import product
```

- Calculates all possible combinations using Cartesian product
- Used for brute force attack

Read more [here.](https://www.geeksforgeeks.org/python-itertools-product/)


## Commands and Arguments 💻

**WARNING** 
- Brute force attacks and the dictionary attack for bcrypt will take a considerable amount of time.

### Brute Force (plain text)
```
-b "user password"
```

### Dictionary Attack (plain text)
```
-d "user password"
```

### Dictionary Attack (md5 hash)
```
-dm "user hash"
```

### Dictionary Attack (sha256 hash)
```
-ds "user hash"
```

### Dictionary Attack (bcrypt hash)
```
-dbc "user hash"
```

### Brute Force (md5 hash)
```
-bm "user hash"
```

### Brute Force (sha256 hash)
```
-bs "user hash"
```

### Brute Force (bcrypt hash)
```
-bbc "user hash"
```

## Example Commands/Formatting
```
python passwordcracker.py -b test

python passwordcracker.py -d asdasd

python passwordcracker.py -dm d16d377af76c99d27093abc22244b342

```




