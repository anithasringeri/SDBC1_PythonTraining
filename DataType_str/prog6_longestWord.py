# Example 6: Finding the longest word
# Objective: Find the longest word in a sentence.
# Outcome: Prints “Longest word: elephant.”
# finding the longest word in a sentence

text="cat dog elephant ant"
longest=""
print(text.split())
print(type(text.split()))
for w in text.split(): # splits the sentence
    if len(w) > len(longest):
        longest=w
    else: 
        print("Longest word:", longest)
