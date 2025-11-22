# Example 6: Word frequency counter
# Objective: Count word frequencies in a sentence; store results in dict; convert to set of unique words.
# Outcome: Prints frequency dictionary and unique words.
# Count word frequency

sentence = "apple banana apple orange"
words = sentence.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
else:
    print("Frequencies:", freq)
    print("Unique words:", set(words))