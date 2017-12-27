import init_data
import operator
import sage.crypto.util
import copy
import utils

# in bytes
def _pad_word(word, size):
    ext_len = size-len(word)%size
    if (len(word) % size != 0):
	word += to_str([chr(0x1)] + [chr(0x0)]*(ext_len-2) + [chr(0x80)]*(ext_len-abs(ext_len-2)-1))
    return word

_j = range(0, init_data.box_size)

def _map_indexed_2d (f, A):
    res = copy.deepcopy(A)
    for x in range(len(A)):
	for y in range(len(A[x])):
	    res[x][y] = f(x, y, A)
    return res

def _theta(A, w = init_data.r):
    def C(x):
	return reduce(operator.xor, map(lambda y: A[x][y], _j))
    def D(x):
	return C((x-1) % init_data.box_size) ^ (rot(C((x+1) % init_data.box_size), 1, w))
    return _map_indexed_2d(lambda x,y,a: a[x][y] ^ D(x), A)

def _ro_pi(A, w = init_data.r):
    B = copy.deepcopy(A)
    for x in _j:
	for y in _j:
	    B[y][(2*x + 3*y) % init_data.box_size] = rot(A[x][y], init_data.r_offsets[x][y], w)
    return B

def _xi(A, w = init_data.r):
    B = _ro_pi(A, w)
    return _map_indexed_2d(
	    lambda x,y,a: B[x][y] ^ ((~B[(x+1) % init_data.box_size][y]) & B[(x+2) % init_data.box_size][y]),
	    A)

def _iota(A, rnd,  w = init_data.r):
    A[0][0] = A[0][0] ^ rnd
    return A

def round(A, rnd, w = init_data.r):
    return _iota(_xi(_theta(A, w), w), rnd, w)
