# !pip install ujson

import codecs
import json

def findKey():
    with open('/content/drive/MyDrive/_data 18 ioan.maftei.json', 'rb') as f:
        fileContent = f.read()
        content = codecs.decode(fileContent, 'utf-8', errors='ignore')
    
    for keyLength in range(5, 10):
        blocks = [content[i:i + keyLength] for i in range(0, len(content), keyLength)]
        
        data = [[] for _ in range(keyLength)]
        for block in blocks:
            for i in range(keyLength):
                if i < len(block):
                    data[i].append(ord(block[i]))
                else:
                    data[i].append(0)
        
        key = ''
        for block in data:
            freq = [0] * 256
            for byte in block:
                if byte < 256:
                    freq[byte] += 1

            #maxFrequency = max(freq)
            xorredByteFreq = max(range(256), key = lambda x: freq[x])

            key += chr(xorredByteFreq ^ ord(' '))
        
        try:
            json.loads(bytes([b ^ k for b, k in zip(content, key.encode())]).decode('utf-8'))
            return key
        except:
            continue

print(f'The key is: {findKey()}')