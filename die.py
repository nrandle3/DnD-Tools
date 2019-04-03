import random as rng


while True: 
	print("-----------------------------------------------------------------")
	x = input("What's your roll: ")
	x = x.split("d")

	rolls = []

	for i in range(1,int(x[0]) + 1):

		rolls.append(rng.randint(1,int(x[1])))

	for i,roll in enumerate(rolls):

		print(str(i+1) + ": " + str(roll))

	print("\nSum:" + str(sum(rolls)))