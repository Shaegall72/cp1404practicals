"""Print asterisks as long as word"""

print("Enter a word longer than 6 letters")
word = input("Word: ")
word_length = len(word)

# ensure word is longer than 6 letters
while word_length <=5:
   print(f"Not long enough, try again")
   word = input("Word: ")
else:

# correct length entered
total_stars = "*" * word_length
print(total_stars)
