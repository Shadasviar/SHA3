import operator

def to_bytestr(word):
    return list(bytearray(word))

def to_str(h):
    if (len(h) < 1):
	return ""
    return reduce(operator.add, h)

def word_to_int(word):
    s = str(sage.crypto.util.ascii_to_bin(word))
    return int(s, base=2)

def split_every (list, n):
    return [list[i:i+n] for i in range(0,len(list), n)]

def pad_with_zero(word, size):
    return word + [0]*(size-len(word))

def split_at(word, n):
    return [word[:n], word[n:]]

def to_fixed_size_bin(a, w):
    num = a.binary()
    return to_str(['0']*(w-len(num))) + num

def rot(W, r, w):
    r = r % w
    b = split_at(to_fixed_size_bin(W, w), r)
    return int(b[1] + b[0], base=2)
