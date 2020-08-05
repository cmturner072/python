#The quick brown fox jumped; count the elements; includes spaces and starts at zero

#T => 0
starter_sentence = 'The quick brown fox jumped'

print(starter_sentence[10])

#output = b

# To replace part of a string using a new variable

starter_sentence = 'The quick brown fox jumped'
first_word = starter_sentence[0:3]

new_sentence = 'Thy' + starter_sentence[3:]
print(new_sentence)

#output = Thy quick brown fox jumped 