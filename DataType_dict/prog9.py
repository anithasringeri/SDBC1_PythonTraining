# Example 9: Using dictionary for word frequency
# Objective: Count occurrences of each word.
# Outcome: Prints “{'apple': 2, 'banana': 1, 'orange': 1}”.
# Count word frequency in a sentence

senprogtence="apple banana apple orange"
freq={} 

for word in sentence.split():
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)