number = int(input())
word = input()

# write a condition for plurals
if number == 1:
    word = word
else:
    word = word + "s"

print(number, word)