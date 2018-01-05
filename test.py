import permutations
import utils
import init_data

_str = "HelloKittyABCDE12345"
pad = utils.pad_word(_str, (1088/8))
words = utils.split_every(pad, (1088/8))
words[0] += utils.to_str([chr(0x0)]*((1600/8)-len(pad)))
s = utils.split_every(words[0], init_data.w/8)
s2 = utils.split_every(s, init_data.box_size)
pseudo_state = map(lambda x: map(lambda y: Integer(utils.word_to_int(y)), x), s2)

def test():

    print "str: ", _str
    print "extended word: ", pad
    print "words: ", words

    print "state: ", pseudo_state

    roundx = permutations.round(pseudo_state, init_data.RC[3])
    print "Round: ", roundx
