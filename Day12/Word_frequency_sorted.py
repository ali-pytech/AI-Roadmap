# Word Frequency Counter
# Counts how many times each word appears in a sentence


sentence = input("Enter any Sentence as String: ")
words = sentence.replace(",","").split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

sorted_frequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)

print("Words Frequency :")

for word, count in sorted_frequency:
    print(f"{word} : {count}")
