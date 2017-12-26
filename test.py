import permutations

_str = "HelloKittyABCDE12345"
_bytestr = _to_bytestr(_str[:])
_extended = _extend_word(_bytestr[:], 1088)
_words = _split_every(_extended[:], init_data.word_len)
_state = _str_to_state(_words[0])
_t = _theta(copy.deepcopy(_state))
_r = _ro(copy.deepcopy(_t))
_p = _pi(copy.deepcopy( _r))
_x = _xi(copy.deepcopy( _p))
_iot = _iota(copy.deepcopy(_x), init_data.RC[2])

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
