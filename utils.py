import operator
import sage.crypto.util

def to_bytestr(word):
    return list(bytearray(word))

# converts list of chars to string
def to_str(h):
    if (len(h) < 1):
	return ""
    return reduce(operator.add, h)

def word_to_int(word):
    s = str(sage.crypto.util.ascii_to_bin(word))
    return int(s, base=2)

# split list for lists of lengths of n
def split_every (list, n):
    return [list[i:i+n] for i in range(0,len(list), n)]

# in bytes
def pad_word(word, size):
    ext_len = size-len(word)%size
    if (len(word) % size != 0):
	word += to_str([chr(0x1)] + [chr(0x0)]*(ext_len-2) + [chr(0x80)]*(ext_len-abs(ext_len-2)-1))
    return word

# prepend word by zeroes, size of resulting word is size
def pad_with_zero(word, size):
    return word + [0]*(size-len(word))

def split_at(word, n):
    return [word[:n], word[n:]]

def to_fixed_size_bin(a, w):
    num = a.binary()
    return to_str(['0']*(w-len(num))) + num

# Bitwise rotation of W with length ow w by r bits to left
def rot(W, r, w):
    r = r % w
    b = split_at(to_fixed_size_bin(W, w), r)
    return int(b[1] + b[0], base=2)
