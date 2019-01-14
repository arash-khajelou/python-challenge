# http://www.pythonchallenge.com/pc/hex/bonus.html

import this

base_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
res_chars = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'

sentence = 'va gur snpr bs jung.'

translator = str.maketrans(base_chars, res_chars)
final_result = sentence.translate(translator)

print(final_result)

# the result is ambiguity
