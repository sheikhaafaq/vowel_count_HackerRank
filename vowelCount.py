def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            #if letter is vowel
            if is_vowel(letter):
                num_vowels += 1
                #if vowel is even
        if num_vowels % 2 == 0:
            score += 2
        else:
            score +=1
    return score

#number of words
n = int(input())
words = input().split()
print(score_words(words))