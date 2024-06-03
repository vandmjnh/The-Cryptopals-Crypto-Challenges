'''Single-byte XOR cipher
https://cryptopals.com/sets/1/challenges/3

The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.
You can do this by hand. But don't: write code to do it for you.
How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.'''

import math

FREQ = {'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
        'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
        'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
        'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182}

def xorBytesConst(b: bytes, const: int) -> bytes:
    return bytes([const ^ _b for _b in b])

def bhattacharyyaDistance(dict1: dict, dict2: dict) -> float:
    bcCoeff = 0
    for letter in FREQ.keys():
        bcCoeff += math.sqrt(dict1[letter] * dict2[letter])
    return -math.log(bcCoeff)

def scoreString(word: bytes) -> float:
    currFreq = {letter: 0 for letter in FREQ.keys()}
    numLetters = 0
    for i in word:
        if chr(i).lower() in FREQ.keys():
            currFreq[chr(i).lower()] += 1
            numLetters += 1
    
    if numLetters != 0:
        currFreq = {letter: val/numLetters for letter, val in currFreq.items()}
    else:
        return 0
    
    distance = bhattacharyyaDistance(FREQ, currFreq)
    return 1 / distance

if __name__ == '__main__':
    src = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

    maxScore = 0
    best_res = b''

    for i in range(2**8):
        tmp = xorBytesConst(src, i)
        score = scoreString(tmp)

        if score > maxScore:
            maxScore = score
            best_res = tmp
    
    print(best_res, f'\n{maxScore=}')
