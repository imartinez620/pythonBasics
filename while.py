nums = list(range(1,100))

#print(nums)

#for num in nums:
#	print(num)

while len(nums) > 0:
	print(nums.pop())

def guessing_game():
	while True:
		print('What is your guess?')
		guess = input()

		if guess == '42':
			print('You correctly guessed it!')
			return False
		else:
			print(f'No, {guess} is not the answer, please try again\n')

guessing_game()