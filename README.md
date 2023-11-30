# programmerApplication
Instructions:
Download the .exe file. Open terminal and navigate to the directory where the .exe file is downloaded. Run ./hangman.exe.

Notes:
The primary challenge that I tried to solve with my code was retaining the correct letters guessed by the user and putting them in the right order. I decided to create an array of strings that held the user's progress. A dash ('-') is used as a placeholder for an unguessed letter. As the user starts to correctly guess letters, the dashes are replaced with the correct letters. A function then converts the array to a string that can be printed more easily. The string is also used

The program decides if a letter is in the correct spot by comparing it to a string called desiredWord. A loop allows the program to iterate through the word and see if there are multiple occurrences of the letter in the word.

I did a bit of data cleanup as well; I trimmed whitespaces and checked if the user input was a single letter.

I used W3 schools to help with Python syntax and had some help uploading this program to GitHub, but the code is all my own.

I think the challenge took be about 6 hours to complete.
