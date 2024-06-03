'''Fixed XOR
https://cryptopals.com/sets/1/challenges/2

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179'''

def fixedXOR(hexString1, hexString2):
    return hex(int(hexString1, 16) ^ int(hexString2, 16))[2:]

def main():
    hexString1 = '1c0111001f010100061a024b53535009181c'
    hexString2 = '686974207468652062756c6c277320657965'
    print(fixedXOR(hexString1, hexString2))

if __name__ == '__main__':
    main()

# Output
'''
746865206b696420646f6e277420706c6179
'''
# The output is correct. The code successfully XORs the two given hex strings.