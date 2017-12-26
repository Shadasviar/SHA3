import permutations

_str = "HelloKittyABCDE12345"
_bytestr = _to_bytestr(_str[:])
_extended = _extend_word(_bytestr[:])
_words = _split_every(_extended[:], init_data.word_len)
_states = map(_str_to_state, _words)
_t = map(_theta, _states)
_r = map(_ro, _t)
_p = map(_pi, _r)
_x = map(_xi, _p)
_iot = map(lambda x: _iota(x, init_data.RC[2]), _x)

def test():
    print "word : ", _str
    print "bytestr: ", _bytestr
    print "extended: ", _extended
    print "splitted: ", _words
    print "states: ", _states
    print "theta: ", _t
    print "ro: ", _r
    print "pi: ", _p
    print "xi: ", _x
    print "iota: ", _iot
