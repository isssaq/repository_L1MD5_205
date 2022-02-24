def sha1(string):

    databits = ''.join(format(ord(i), '08b') for i in string)
    databits += ''.join(format(1, '01b'))

    binstring = databits
# len(binstring) = 448
    while len(binstring) % 512 != 448:
        binstring += '0'
#

# len(padded_bin_length) = 64
# Error: format(len(string), '064b')
# Take a length of string bits, NOT string's length
    padded_bin_length = (format(len(databits)-1, '064b'))
    binstring += padded_bin_length

# func to shift on b bits
    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

# break binstring in chunks
    def divide_chunks(l, n):
        for i in range(0,len(l),n):
            yield l[i:i+n]
            
# n = 32
# variables
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    for c in divide_chunks(binstring, 512):
        words80 = divide_chunks(c, 32)
        words80 = list(words80)
        w = [0]*80
        for n in range(0, 16):
            w[n] = int(words80[n], 2)
        for i in range(len(words80), 80):
            temp = w[i-3] ^ w[i - 8] ^ w[i - 14] ^ w[i-16]
            w[i] = rol(temp, 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        # Main loop
        for j in range(0, 80):
            if j < 20:
                f = (b & c) | (~(b) & d)
                k = 0x5A827999
            elif j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif j < 80:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            tmp =(rol(a, 5) + f + e + k + w[j] & 0xffffffff)
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = tmp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    
    hashes = [h0, h1, h2, h3, h4]
    res = ''
    for h in hashes:    
        res += '%08x' % h

    return res
