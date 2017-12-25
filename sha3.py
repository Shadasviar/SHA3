import init_data

def _extend_word(word, size):
    res = list(bytearray(word))
    ext_len = size-len(res)%size
    if (len(res) % size != 0):
        res += [0x1] + [0x0]*(ext_len-2) + [0x80]*(ext_len-abs(ext_len-2)-1)
    return res

def _split (n, list):
    return [list[i:i+n] for i in range(0,len(list), n)]

_j = range(0, init_data.box_size)

# apply f(i,j,k,a) for every element of A with k from 0 to w
def _map_indexed (f, A, w):
    _k = range(0,w)
    res = A
    for i in _j:
        for j in _j:
            for k in _k:
                res[i][j][k] = f(i, j, k, A)
    return res

def _theta (A, w):
    def C(i, k):
        return reduce(operator.xor, map(lambda x: A[i][x][k], _j))
    def D(i, k):
        return C((i-1) % 5, k) ^ C((i+1) % 5, (k-1) % w)

    return _map_indexed(lambda i,j,k,a: a[i][j][k] ^ D(i,k), A, w)

def _ro (A, w):
    _k = range(0,w)
    res = A
    for k in _k:
        res[0][0][k] = A[0][0][k]
    t = range(0,24)
    (i, j) = (1,0)
    for k in _k:
        res[i][j][k] = A[i][j][(k - (t + 1)*(t + 2)/2) % w]
        (i,j) = (j, (2*i + 3*j) % 5)
    return res

def _pi (A, w):
    return _map_indexed(lambda i,j,k,a: a[(i + 3*j) % 5][i][k], A, w)

def _xi (A, w):
    return _map_indexed(lambda i,j,k,a: a[i][j][k] ^ ((a[(i+1) % 5][j][k] ^ 1) * a[(i+2) % 5][j][k]), A, w)

def _iota (A, rnd, w):
    _k = range(0,w)
    res = A
    for k in _k:
        res[0][0][k] = A[0][0][k] ^ rnd

def _str_to_state (S, w):
    return _map_indexed(
            lambda i,j,k,a: (5*i + j) * w + S[k], 
            [[range(0,w)] * (_j[-1]+1)] * (_j[-1]+1),
            w)
