def greeting(time_of_the_day, *args, **kwargs):
	print(f"Hi {' '.join(args)}, I hope that you having a great {time_of_the_day}")

	if kwargs:
		print('Your task for the day are:')
		for key, val in kwargs.items():
			print(f'{key} => {val}')


greeting('Morning', 
		'Peter', 'Parker',
		first_task = 'Empty dishwasher',
		second_task = 'Take pupper aoutside',
		third_task = 'Math homework'
		)