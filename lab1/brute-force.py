# !pip install ujson

import ujson
import itertools
import multiprocessing

with open("/content/drive/MyDrive/_data 18 ioan.maftei.json", 'rb') as f:
    content = f.read().decode("utf8")

def generateKeysOneByOne():
    upperAndLowerLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keys = []
    for i in range(5, 10):
        for key in itertools.product(upperAndLowerLetters, repeat=i):
            yield ''.join(key).encode()

def decrypt():
    pool = multiprocessing.Pool(processes = 4)

    for key, plaintext in pool.imap_unordered(checkIfDecrypted, ((key, content) for key in generateKeysOneByOne())):
        if plaintext is not None:
            print("Key is: ", key)
            with open('/content/drive/MyDrive/plaintext.json', 'w') as f:
                f.write(plaintext)
            return

def checkIfDecrypted(params):
    key, content = params
    plaintext = bytes([content[j] ^ key[j % len(key)] for j in range(len(content))])
    try:
        ujson.loads(plaintext)
        return key, plaintext
    except ValueError:
        return key, None

decrypt()
