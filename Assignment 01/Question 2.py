def A_Sentence(sentence):
    words = sentence.split()
    total_w = len(words)
    total_ch = len(sentence)
 
    longest = words[0]
    shortest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
        if len(w) < len(shortest):
            shortest = w
 
    vowels = 0
    for ch in sentence:
        if ch in "aeiouAEIOU":
            vowels += 1
 
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    return total_w, total_ch, longest, shortest, vowels, unique_words, sorted_words
 
 
sentence = input("Enter a sentence: ")
tw, tc, lw, sw, v, uw, sorted_w = A_Sentence(sentence)
 
print("Total words:", tw)
print("Total characters:", tc)
print("Longest word:", lw)
print("Shortest word:", sw)
print("Vowels:", v)
print("Unique words:", uw)
print("Alphabetical:", sorted_w)
 
with open("word_analysis.txt", "w") as f:
    f.write("Sentence: " + sentence + "\n")
    f.write("Total words: " + str(tw) + "\n")
    f.write("Total characters: " + str(tc) + "\n")
    f.write("Longest word: " + lw + "\n")
    f.write("Shortest word: " + sw + "\n")
    f.write("Vowels: " + str(v) + "\n")
    f.write("Unique words: " + str(uw) + "\n")
    f.write("Alphabetical order: " + ", ".join(sorted_w) + "\n")
