import nltk
from nltk import ngrams
# Given a list of words, return a dictionary where the keys are the words and the values are the number of times the word appears in the list.

def CountOccurence(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("%s : %s"%(key, value))

CountOccurence(['abc','abc','bac','adw','adw','bac','hello','wello'])

# Given a list of words, return a dictionary where the keys are the words and the values are the number of letters in the word.

def wordCount(my_list):
  freq={}
  for item in my_list:
    if (item in freq):
      continue
    else:
      freq[item]=len(item)

  for key,value in freq.items():
    print("%s : %s"%(key,value))


wordCount(['abc','abc','bac','adw','adw','bac','hello','wello'])

# Given a list of words, return a dictionary where the keys are the words and the values are the number of vowels in the word.

#Reference: https://stackoverflow.com/questions/32569722/creating-a-dictionary-from-a-string-where-the-values-are-the-vowel-counts-from-e#:~:text=vowel_count%20%3D%20%7Bi%3A%20sum(c.lower()%20in%20%27aeiou%27%20for%20c%20in%20i)%20for%20i%20in%20split%7D

m_list=['abc','abc','bac','adw','adw','bac','hello','wello']
vowel_count = {i: sum(c.lower() in 'aeiou' for c in i) for i in m_list}
print(vowel_count)

# Redo one with all the punctuation removed and all words lower cased.

def CountOccurence(my_list):
    freq = {}
    for item in my_list:
        item=item.translate(str.maketrans('','',',?!.'))
        item=item.lower()
        if(item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("%s : %s"%(key, value))

CountOccurence(['aBc','abc','Bac','adW','adw','bac','hello','wello','AbC!!'])

# Given some text (containing multiple sentences) find the frequency of bigrams (pairs of words) and trigrams (triple words)

#References:
# https://www.datasciencelearner.com/count-bigrams-in-nltk-stepwise-solution/
# https://stackoverflow.com/questions/17531684/n-grams-in-python-four-five-six-grams


sentence = 'this is a this is a foo bar sentences and i want to ngramize it'

bigrams = ngrams(sentence.split(), 2)
trigrams=ngrams(sentence.split(), 3)

frequency = nltk.FreqDist(bigrams)
for key,value in frequency.items():
    print(key,value)

print('\n\n')
frequency = nltk.FreqDist(trigrams)
for key,value in frequency.items():
    print(key,value)

# Write a generic function to create n grams (where n can be 1 to 5).
def nGram(sentence,n):
  sixgrams = ngrams(sentence.split(), n)
  frequency = nltk.FreqDist(sixgrams)
  for key,value in frequency.items():
      print(key,value)
nGram('this is a foo bar sentences and i want to ngramize it',3)

