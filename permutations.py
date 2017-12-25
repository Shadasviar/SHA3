import init_data
import operator

def _to_bytestr(word):
    return list(bytearray(word))

def _extend_word(word, size = 64):
    ext_len = size-len(word)%size
    if (len(word) % size != 0):
        word += [0x1] + [0x0]*(ext_len-2) + [0x80]*(ext_len-abs(ext_len-2)-1)
    return word

def _split_every (list, n = 64):
    return [list[i:i+n] for i in range(0,len(list), n)]

_j = range(0, init_data.box_size)

# apply f(i,j,k,a) for every element of A with k from 0 to w
def _map_indexed (f, A, w = 64):
    _k = range(0,w)
    res = A
    for i in _j:
        for j in _j:
            for k in _k:
                res[i][j][k] = f(i, j, k, A)
    return res

def _theta (A, w = 64):
    def C(i, k):
        return reduce(operator.xor, map(lambda x: A[i][x][k], _j))
    def D(i, k):
        return C((i-1) % init_data.box_size, k) ^ C((i+1) % init_data.box_size, (k-1) % w)

    return _map_indexed(lambda i,j,k,a: a[i][j][k] ^ D(i,k), A, w)

def _ro (A, w = 64):
    _k = range(0,w)
    res = A
    for k in _k:
        res[0][0][k] = A[0][0][k]
    t_range = range(0,24)
    (i, j) = (1,0)
    for t in t_range:
	for k in _k:
	    res[i][j][k] = A[i][j][(k - (t + 1)*(t + 2)/2) % w]
	    (i,j) = (j, (2*i + 3*j) % init_data.box_size)
    return res

def _pi (A, w = 64):
    return _map_indexed(lambda i,j,k,a: a[(i + 3*j) % init_data.box_size][i][k], A, w)

def _xi (A, w = 64):
    return _map_indexed(
	    lambda i,j,k,a: a[i][j][k]
	    ^ ((a[(i+1) % init_data.box_size][j][k] ^ 1)
		* a[(i+2) % init_data.box_size][j][k]),
	    A, w)

def _iota (A, rnd, w = 64):
    _k = range(0,w)
    res = A
    for k in _k:
	res[0][0] = map(operator.xor, A[0][0], map(lambda x: rnd & (1 << x), range(0,w)))
    return res

def _str_to_state (S, w = 64):
    return _map_indexed(
            lambda i,j,k,a: (init_data.box_size*i + j) * w + S[k], 
	    [[[a for a in range(w)] for c in _j] for d in _j],
            w)
