# Example 5: Counting occurrences of a word
# Objective: Count how many times a word appears.
# Outcome: Prints “Word 'apple' occurs 2 times.”

#count occurence of apple

sentence ="apple banana apple orange"
words=sentence.split()
count=0
for w in words:
    if w=="apple":
        count+=1
    else:
        print("Word 'apple' occurs.", count, "times")