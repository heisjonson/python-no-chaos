word = input("Enter a word: ")

reverse_word = ""

for letter in range(len(word)):
    reverse_word = word[letter] + reverse_word

print(reverse_word)

if word == reverse_word:
    print("This is a palindrome")
else:
    print("This is not a palindrome")