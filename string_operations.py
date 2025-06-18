"""
This script demonstrates various string manipulation techniques in Python
using the example phrase: " Python is powerful and fun! ".

The operations performed include:
- Printing the original phrase and its length
- Stripping leading and trailing whitespace
- Converting to uppercase and lowercase
- Checking for the presence of a specific word
- Finding the index of a substring ("fun")
- Replacing a word with another
- Splitting the phrase into a list of words
- Joining the words with a hyphen
- Printing specific character slices
- Reversing the string using slicing

This script is a useful reference for basic string operations and slicing.
"""

main_phrase = " Python is powerful and fun! "

print(f"This is the main phrase: {main_phrase}")
print(f"The length of main phrase: {len(main_phrase)}")

cleaned_phrase = main_phrase.strip()
print(f"This is stripped main phrase: {cleaned_phrase}")

upper_phrase = cleaned_phrase.upper()
print(f"This is the upper phrase: {upper_phrase}")

lower_phrase = cleaned_phrase.lower()
print(f"This is the lower phrase: {lower_phrase}")

if "powerful" in cleaned_phrase:
  print(f"The word 'powerful' is found.")

fun_index = cleaned_phrase.find("fun")
print(f"Index of 'fun': {fun_index}")

modified_phrase = cleaned_phrase.replace("fun", "awesome")
print(f"This is the modified phrase: {modified_phrase}")

words_list = cleaned_phrase.split(" ")
print(f"Words in cleaned phrase as list: {words_list}")

hyphenated_phrase = "-".join(words_list)
print(f"Hyphenated phrase: {hyphenated_phrase}")

print(f"The first six characters of cleaned phrase are: {cleaned_phrase[0:6]}")
print(f"The 7 to 14 characters of cleaned phrase are: {cleaned_phrase[7:14]}")
print(f"Reversed cleaned phrase: {cleaned_phrase[::-1]}")