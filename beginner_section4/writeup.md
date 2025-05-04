# PW Crack 4 Writeup
Inspect the code of the python script `level4.py`
How `level4.py` works:
1. Reads both the encoded version of the flag file and correct password hash file
2. Ask user for correct password out of 100 in the list
3. If the user chose the correct password, decode the flag using the correct password as the key.
4. Return the decoded flag to the user via `print()`.

There's also a process where it hashes and encodes your input as an MD5 hash, and is used in the `level_4_pw_check()` method to turn your input (a string) into an iteratable object and turn it into an MD5 hashed object.

# Solution
Using an external python script to crack the password. Other solutions are possible, but this made the most sense to me rather than changing the source code of `level4.py`.

I am given the correct password's hash value as part of the challenge, and I'm also provided the possible passwords near the bottom of `level4.py`.

I can copy the hashing process of the user's input in `level4.py`, and compare that hash against the correct once, since it's available to me.

1. Read in the correct hash in binary mode
2. Copy the input hashing function to my script
3. Loop through the possible password list, if current iteration matches the correct hash, print it.
4. Das it
