import random

print("Welcome to the game!")

continueGame = bool(5)
words = ["chapstick", "flower", "magnesium", "programmer", "emerald", "smart", "zebra", "ravioli", "chair", "red"]
placeholder = "-"


def create_current_progress(current_progress, correct_letters_guessed):
	current_progress = str()
	for y in range(len(correct_letters_guessed)):
		current_progress += correct_letters_guessed[y]
	return current_progress


while continueGame:

	# ends game if user has guessed all the words
	if len(words) == 0:
		break

	# selects a random word and removes it from the array
	randWordsIndex = random.randint(0, len(words) - 1)
	desiredWord = words[randWordsIndex]
	words.pop(randWordsIndex)

	# resets variables
	numIncorrectGuesses = 0
	numCorrectGuesses = 0

	correctLettersGuessed = []
	incorrectLettersGuessed = []

	currentProgress = str()

	# creates an array of dash placeholders in correctLettersGuessed
	for x in range(len(desiredWord)):
		correctLettersGuessed.append(placeholder)

	# prints length of word for user
	print("\nThe word has " + str(len(desiredWord)) + " letters.")

	# creates a variable to check for placeholder
	placeholderIndex = correctLettersGuessed.index(placeholder)

	# loops while game is unfinished (placeholder(s) still in correctLettersGuessed)
	while placeholderIndex > -1:

		# gets user guess and cleans data
		userGuess = input("Please guess a single letter.\n").strip().lower()

		# checks in user input is a single letter
		if (not userGuess.isalpha()) or len(userGuess) > 1:
			continue

		# checks if userGuess is in desiredWord
		userGuessIndex = desiredWord.find(userGuess)

		# checks if userGuess is correct (userGuessIndex is not -1)
		if userGuessIndex > -1:

			# loops until all occurrences of userGuess are found
			while userGuessIndex > -1:
				# replaces placeholders with correct letters
				correctLettersGuessed[userGuessIndex] = userGuess
				# looks for multiple occurrences of userGuess
				userGuessIndex = desiredWord.find(userGuess, userGuessIndex + 1)

			# increments number of correct guesses
			numCorrectGuesses += 1

			currentProgress = create_current_progress(currentProgress, correctLettersGuessed)

			print("\nGood guess! Here is your progress so far:\n" + currentProgress)

		# if userGuess is incorrect
		else:

			# increments incorrect number of guesses
			numIncorrectGuesses += 1

			# adds incorrect guess to incorrectLettersGuessed array
			incorrectLettersGuessed.append(userGuess)

			# prints incorrect letter
			print("\nThe letter " + userGuess + " is not in the word.")

			# prints ALL incorrect letters
			for x in range(len(incorrectLettersGuessed)):
				print(incorrectLettersGuessed[x] + " ", end="")

		# prints number of correct and incorrect guesses
		print("\nNumber of correct guesses: " + str(numCorrectGuesses))
		print("Number of incorrect guesses: " + str(numIncorrectGuesses) + "\n")

		# clears currentProgress string and checks to see if there are still placeholders
		currentProgress = create_current_progress(currentProgress, correctLettersGuessed)

		placeholderIndex = currentProgress.find(placeholder)

	# tells the user they guessed the word and how many guesses it took
	totalGuesses = numCorrectGuesses + numIncorrectGuesses
	print("Congrats! You guessed the word. You took " + str(totalGuesses) + " guesses.")

	# checks if user wants another word
	userDesire = input("\nWould you like to play again?\n")

	# checks if user wants to keep playing the game
	if userDesire != "Yes":
		continueGame = False

# tells the user if they have completed all the words
if len(words) == 0:
	print("\nYou have guessed all the words in the game.")

# thanks the user and ends the game
print("\nThank you for playing!")
