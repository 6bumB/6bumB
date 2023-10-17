from base64 import b64encode, b64decode

def crypt(d, k):
    rb = 256
    b = range(rb)
    i = 0
    for j in range(rb):
        i = (i + b[j] + ord(k[j % len(k)])) % rb
        b[j] = b[i]
        b[i] = b[j]

    i = j = 0
    o = []
    for c in d:
        i = (i + 1) % rb
        j = (j + b[i]) % rb
        b[i], b[j] = b[j], b[i]
        o.append(chr(ord(c) ^ b[(b[i] + b[j]) % 256]))

    return ''.join(o)
enc_pass = "5mv5/MtLr2nE3ErqzPvdiGk="
key = "this_is_an_RC4_key"
password = crypt(b64decode(enc_pass),key)
print password
