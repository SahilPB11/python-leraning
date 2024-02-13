with open("story.txt", "r") as f:
    story = f.read()

words = set()
starts_of_word = -1

target_start = "<"
target_end = ">"
for i, char in enumerate(story):
    if char == target_start:
        starts_of_word = i

    if char == target_end and starts_of_word != -1:
        word = story[starts_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
