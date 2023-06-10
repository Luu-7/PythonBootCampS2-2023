# BootCamp Q2 - Guess Random Number
import random
def rules():
	print("Welcome to Guess the Number!")
	print("==========================================")
	print('''Rules: 
	1. Guess must be from 0 - 100
	2. Guess must be an integer
	3. Unlimited Guesses 
	''')
	print("==========================================")

def game():
	answer = random.randint(0,100)
	# print(answer)
	while True:
		try:
			UserInput = int(input(">> Guess: "))
			if UserInput >= 0 and UserInput < answer :
				print("Too low")
			elif UserInput > answer and UserInput <= 100:
				print("Too high")
			elif UserInput == answer: 
				print("Correct! The answer is", str(answer))
				return()
			else:
				print("Guess must be between 0 - 100 (inclusive). Try Again")
		except:
			print("Invalid guess. Try again")	
			
if __name__ == "__main__":
	# Enter test code below
	rules()
	game()
