from permutations import round
from functools import partial
import init_data
import utils
import copy

def keccak_f(A):
    for i in range(init_data.n_rounds):
        A = round(A, init_data.RC[i])
    return A

def keccak(word, r = 1088, c = 512, d = 256):
    if (r+c != 1600):
        raise Exception("r+c must be 1600")

    init_data.b = r+c
    P = utils.pad_word(word, r/8)
    P = utils.split_every(P, init_data.w/8)
    P = map(lambda x: utils.word_to_int(x), P)
    P = utils.split_every(P, r/init_data.w)
    P = map(partial(utils.pad_with_zero, size = (r+c)/init_data.w), P)

    S = [[0]*5 for i in range(init_data.box_size)]

    for Pi in P:
        S = utils.split_every(Pi, init_data.box_size)
        S = keccak_f(S)

    Z = []
    while (len(Z) < d/64):
        Z = utils.to_str(S)
        S = keccak_f(S)

    return utils.to_str(map(lambda x: format(x, 'x'), Z[:d/64]))

SHA3_256 = keccak
