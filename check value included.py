sentence = "The quick brown fox jumped over the lazy Dog"
word= 'dog'

if word in sentence.lower():
	print('The word was found in the sentence')
else:
	print('The word was not in the sentence')

######################################################

nums = [1,2,3,4]

if 0 in nums:
	print('The number was found')
else:
	print('The number was not found')