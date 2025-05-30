import hashlib, sys

# read in the correct hash's value
correct_hash = open('level4.hash.bin', 'rb').read()

# copy from possible pw list in main script
pos_pw_list = ["8c86", "7692", "a519", "3e61", "7dd6", "8919", "aaea", "f34b", "d9a2", "39f7", "626b", "dc78", "2a98", "7a85", "cd15", "80fa", "8571", "2f8a", "2ca6", "7e6b", "9c52", "7423", "a42c", "7da0", "95ab", "7de8", "6537", "ba1e", "4fd4", "20a0", "8a28", "2801", "2c9a", "4eb1", "22a5", "c07b", "1f39", "72bd", "97e9", "affc", "4e41", "d039", "5d30", "d13f", "c264", "c8be", "2221", "37ea", "ca5f", "fa6b", "5ada", "607a", "e469", "5681", "e0a4", "60aa", "d8f8", "8f35", "9474", "be73", "ef80", "ea43", "9f9e", "77d7", "d766", "55a0", "dc2d", "a970", "df5d", "e747", "dc69", "cc89", "e59a", "4f68", "14ff", "7928", "36b9", "eac6", "5c87", "da48", "5c1d", "9f63", "8b30", "5534", "2434", "4a82", "d72c", "9b6b", "73c5", "1bcf", "c739", "6c31", "e138", "9e77", "ace1", "2ede", "32e0", "3694", "fc92", "a7e2"]

def hash_pw(pw_str):
    ba = bytearray() # create byte array
    ba.extend(pw_str.encode()) # populate bytearray with string info encoded as UTF-8
    m = hashlib.md5() # create hash object
    m.update(ba) # provide data from input to hash object
    return m.digest() # generate and return the digest

for pw in pos_pw_list: # loop the entire length of password candidates
    if hash_pw(pw) == correct_hash: # if the hashed version of input matches the correct hash
        print(f"Correct password: {pw}") # fstring prints the password
        break # stop execution

