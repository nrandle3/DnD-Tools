import random as rng
import re
import sys
python3 = True
if sys.version_info[0] < 3:
    python3 = False

dicePattern = re.compile("^\d+d\d+$")

print("Welcome!")
print("The input takes the number of dice, a lowercase 'd' and the faces of the die")
print("E.g Throw two 20 sided dice: 2d20")
print("Type exit to finish")

while True:
	print("-----------------------------------------------------------------")
	if python3:
		x = input("What's your roll: ")
	else:
		x = raw_input("What's your roll: ")
	if not bool(dicePattern.match(x)):
		if x == "exit":
			break
		print("Invalid value (e.g. 4d6)")
		continue
	x = x.split("d")

	rolls = []

	for i in range(1,int(x[0]) + 1):

		rolls.append(rng.randint(1,int(x[1])))

	for i,roll in enumerate(rolls):

		print(str(i+1) + ": " + str(roll))

	print("\nSum:" + str(sum(rolls)))
