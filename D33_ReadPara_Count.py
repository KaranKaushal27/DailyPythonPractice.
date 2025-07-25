import string
paragraph = input("Enter a para : ")

cleaned_para = paragraph.lower()
for punct in string.punctuation:
    cleaned_para = cleaned_para.replace(punct,"")

words = cleaned_para.split()

total_words = len(words)
unique_words = set(words)
unique_count = len(unique_words)

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] +=1
    else:
        word_freq[word] = 1
    
print("\n --analysis--")
print("Total words: ", total_words)
print("unique words", unique_count)
print("word frequecies : ")

for word, freq in word_freq.items():
    print(f"{word}: {freq}")
