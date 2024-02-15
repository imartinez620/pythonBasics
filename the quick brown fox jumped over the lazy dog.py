sentence = "the quick brown fox jumped over the lazy dog"
sentence_two = 'That is my dog\'s bowl'
sentence_three = "That is my dog's bowl"
sentence_four = "Tiffany said, \"That is my dog\'s bowl\""
sentence_five = "the quick brown fox jumped over the lazy dog".upper()
sentence_six = "the quick brown fox jumped over the lazy dog".capitalize()

print(sentence)
print(sentence_two)
print(sentence_three)
print(sentence_four)
print(sentence_five)
print(sentence_six)

new_sentence = "THE" + sentence[3:]

print(new_sentence)